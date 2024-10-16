import itertools
from typing import Dict, List, Tuple, Any
from itertools import product

class Node:
    def __init__(self, name: str, cpt: Dict[tuple, float]):
        self.name = name
        self.parents = []  # Initialized with no parents
        self.children = []  # Initialized with no children
        self.cpt = cpt  # Conditional Probability Table (CPT)
        self.states = []

    def __repr__(self):
        return f"Node({self.name})"



class Factor:
    def __init__(self, variables: List[str], cpt: Dict[Tuple, float]):
        self.variables = variables  # The variables that this factor covers
        self.cpt = cpt  # The conditional probability table, as a dictionary

    def restrict(self, evidence: Dict[str, str]) -> 'Factor':
        """
        Restrict this factor to the provided evidence.
        """
        new_cpt = {}
        for assignment in self.cpt:
            if all((evidence.get(var) == val or var not in evidence) for var, val in zip(self.variables, assignment)):
                # Restrict to evidence by only keeping the assignments consistent with the evidence
                new_assignment = tuple(val for var, val in zip(self.variables, assignment) if var not in evidence)
                new_cpt[new_assignment] = self.cpt[assignment]
        new_variables = [var for var in self.variables if var not in evidence]
        return Factor(new_variables, new_cpt)

    def multiply(self, other: 'Factor') -> 'Factor':
        """
        Multiply this factor with another factor.
        """
        # Find the variables common to both factors
        common_vars = set(self.variables) & set(other.variables)
        new_variables = list(set(self.variables) | set(other.variables))
        
        new_cpt = {}
        for self_assignment in self.cpt:
            for other_assignment in other.cpt:
                if all(self_assignment[self.variables.index(var)] == other_assignment[other.variables.index(var)] for var in common_vars):
                    # Combine assignments from both factors for non-common variables
                    new_assignment = tuple()
                    for var in new_variables:
                        if var in self.variables:
                            new_assignment += (self_assignment[self.variables.index(var)],)
                        else:
                            new_assignment += (other_assignment[other.variables.index(var)],)
                    new_cpt[new_assignment] = self.cpt[self_assignment] * other.cpt[other_assignment]
        
        return Factor(new_variables, new_cpt)

    def sum_out(self, variable: str) -> 'Factor':
        """
        Sum out a variable from this factor.
        """
        if variable not in self.variables:
            return self  # If the variable is not in this factor, return the factor as is
        
        new_variables = [var for var in self.variables if var != variable]
        new_cpt = {}
        for assignment in self.cpt:
            new_assignment = tuple(val for var, val in zip(self.variables, assignment) if var != variable)
            new_cpt[new_assignment] = new_cpt.get(new_assignment, 0) + self.cpt[assignment]
        
        return Factor(new_variables, new_cpt)

    def normalize(self) -> 'Factor':
        """
        Normalize this factor so that the sum of all probabilities is 1.
        """
        total = sum(self.cpt.values())
        new_cpt = {assignment: prob / total for assignment, prob in self.cpt.items()}
        return Factor(self.variables, new_cpt)

    def __repr__(self):
        return f"Factor({self.variables})"

    


class BayesianNetwork:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node: Node):
        if node.name in self.nodes:
            raise ValueError(f"Node {node.name} already exists.")
        self.nodes[node.name] = node
    
    def add_edge(self, parent_name: str, child_name: str):
        if parent_name not in self.nodes or child_name not in self.nodes:
            raise ValueError("Both nodes must be added before creating an edge.")
        self.nodes[child_name].parents.append(parent_name)
        self.nodes[parent_name].children.append(child_name)
    
    def get_node(self, name: str) -> Node:
        if name in self.nodes:
            return self.nodes[name]
        else:
            raise ValueError(f"Node {name} not found in the network.")

    def number_of_edges(self):
        return sum(len(node.parents) for node in self.nodes.values())

    def number_of_parameters(self):
        # Calculate the number of parameters for the entire network
        num_params = 0
        for node in self.nodes.values():
            # The number of parameters is the product of the number of states of the parents
            # times the number of states of the node minus one (since they must sum to 1)
            if node.parents:
                parent_states_combinations = product(*[range(len(self.nodes[parent].states)) for parent in node.parents])
                num_params += (len(node.states) - 1) * len(list(parent_states_combinations))
            else:
                # For nodes without parents, the number of parameters is the number of states minus one
                num_params += len(node.states) - 1
        return num_params

    def average_degree(self):
        # Twice the number of edges divided by the number of nodes gives the average degree
        return 2 * self.number_of_edges() / len(self.nodes)

    def max_parents(self):
        return max(len(node.parents) for node in self.nodes.values())

    def average_markov_blanket_size(self):
        total_size = 0
        for node in self.nodes.values():
            # The Markov blanket consists of the node's parents, its children, and the parents of its children (its spouses)
            blanket = set(node.parents)  # Start with the parents
            blanket.update(node.children)  # Add the children

            # Now add the spouses (other parents of the children) if they are not the node itself
            for child in node.children:
                blanket.update(parent for parent in self.nodes[child].parents if parent != node.name)

            total_size += len(blanket)  # Add the size of this node's Markov blanket

        # Return the average size
        return total_size / len(self.nodes) if self.nodes else 0

    def print_details(self):
        print(f"Number of nodes: {len(self.nodes)}")
        print(f"Number of edges: {self.number_of_edges()}")
        print(f"Number of parameters: {self.number_of_parameters()}")
        print(f"Average degree: {self.average_degree():.2f}")
        print(f"Maximum number of parents: {self.max_parents()}")
        print(f"Average Markov blanket size: {self.average_markov_blanket_size():.2f}")

    def __repr__(self):
        return f"BayesianNetwork({len(self.nodes)} nodes)"
    

    def print_network(self):
        for node_name, node in self.nodes.items():
            print(f"Node: {node_name}")
            
            if node.parents:
                parents_str = ', '.join(node.parents)
                print(f"  Parents: {parents_str}")
            else:
                print("  Parents: None")
            
            if node.children:
                children_str = ', '.join(node.children)
                print(f"  Children: {children_str}")
            else:
                print("  Children: None")
            
            if node.cpt:
                print("  CPT:")
                # Each key in the CPT dictionary is a tuple of states.
                # The last element of the tuple is the node's own state, and the others are the parent states.
                for states, prob in node.cpt.items():
                    parent_states = states[:-1]  # Extract parent states
                    node_state = states[-1]  # Extract node's own state
                    if parent_states:  # If there are parent states, print them
                        parent_states_str = ', '.join(parent_states)
                        print(f"    P({node.name}={node_state} | {parent_states_str}) = {prob}")
                    else:  # If there are no parent states, print only the node's state probability
                        print(f"    P({node.name}={node_state}) = {prob}")
            else:
                print("  CPT: None")
            
            print()  # Print an empty line for better readability 

    def get_cpt(self):
        for node_name, node in self.nodes.items():
            if node.cpt:
                print

    def node_to_factor(self, node_name: str) -> Factor:
        """Utility function to convert a node's CPT into a factor."""
        node = self.get_node(node_name)
        # Create a list of variables for the factor, including the node and its parents
        variables = node.parents + [node.name]

        # Create a CPT for the factor with keys representing the full variable assignment
        # Convert the tuples from the node's CPT to have full assignments as expected by the Factor class
        factor_cpt = {}
        for assignment, prob in node.cpt.items():
            # Extend the assignment with all combinations of the node's states if it's not a leaf node
            if node.children:
                for state in node.states:
                    new_assignment = assignment + (state,)
                    factor_cpt[new_assignment] = prob
            else:
                factor_cpt[assignment] = prob

        # Return the factor representation of the node
        return Factor(variables, factor_cpt)

    def variable_elimination(self, query: List[str], evidence: Dict[str, str]) -> Factor:
        factors = {node_name: self.node_to_factor(node_name) for node_name in self.nodes}

        # 1. Restrict Factors based on evidence
        for var, value in evidence.items():
            new_factors = {}
            for factor in factors.values():
                if var in factor.variables:
                    restricted_factor = factor.restrict({var: value})
                    new_factors[tuple(restricted_factor.variables)] = restricted_factor
                else:
                    new_factors[tuple(factor.variables)] = factor
            factors = new_factors

        # 2. Eliminate Irrelevant Variables
        all_variables = set().union(*(f.variables for f in factors.values()))
        irrelevant_vars = all_variables - set(query) - set(evidence.keys())

        # New ordering heuristic based on the fewest edges
        def variable_ordering(variables):
            # Sort the variables based on the number of edges in the graph
            return sorted(variables, key=lambda var: len(self.nodes[var].parents) + len(self.nodes[var].children))

        ordered_irrelevant_vars = variable_ordering(irrelevant_vars)

        for var in ordered_irrelevant_vars:
            # Find factors that actually contain the variable
            factors_containing_var = {tuple(f_vars): f for f_vars, f in factors.items() if var in f_vars}

            if factors_containing_var:
                # Multiply factors containing the variable
                factor_keys = list(factors_containing_var.keys())
                product = factors[factor_keys[0]]
                for factor_vars in factor_keys[1:]:
                    product = product.multiply(factors[factor_vars])

                # Sum out the variable
                new_factor = product.sum_out(var)

                # Remove old factors and add the new one
                for factor_vars in factor_keys:
                    del factors[factor_vars]
                factors[tuple(new_factor.variables)] = new_factor

        # 3. Multiply Remaining Factors
        final_factor = None
        for factor in factors.values():
            if final_factor is None:
                final_factor = factor
            else:
                final_factor = final_factor.multiply(factor)

        # 4. Normalize the result
        result_factor = final_factor.normalize()

        return result_factor




#test code can be ignored
# # Define the Conditional Probability Tables (CPTs)
# binary_cpt_a = {
#     (True,): 0.9,
#     (False,): 0.1
# }

# binary_cpt_b_given_a = {
#     (True, True): 0.8,
#     (True, False): 0.2,
#     (False, True): 0.3,
#     (False, False): 0.7
# }

# non_binary_cpt_c_given_b = {
#     (True, 'LOW'): 0.95,
#     (True, 'NORMAL'): 0.04,
#     (True, 'HIGH'): 0.01,
#     (False, 'LOW'): 0.5,
#     (False, 'NORMAL'): 0.3,
#     (False, 'HIGH'): 0.2
# }

# # Instantiate the Bayesian Network nodes
# node_a = Node('A', binary_cpt_a)
# node_b = Node('B', binary_cpt_b_given_a)
# node_c = Node('C', non_binary_cpt_c_given_b)

# # Define the states for each node
# node_a.states = [True, False]
# node_b.states = [True, False]
# node_c.states = ['LOW', 'NORMAL', 'HIGH']

# # Instantiate the Bayesian Network
# bn = BayesianNetwork()

# # Add the nodes to the network
# bn.add_node(node_a)
# bn.add_node(node_b)
# bn.add_node(node_c)

# # Define the edges between nodes
# bn.add_edge('A', 'B')
# bn.add_edge('B', 'C')



# # Test variable elimination
# query = ['C']  # Query for the probability distribution of Node C
# evidence = {'A': True}  # Evidence that Node A is true

# # Perform variable elimination
# result_factor = bn.variable_elimination(query, evidence)

# # Output the resulting factor and its CPT
# print(result_factor)
# print(result_factor.cpt)