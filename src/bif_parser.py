import os
import re
from bayesian_network import BayesianNetwork, Node

def parse_cpt(cpt_lines, states):
    cpt_value_pattern = re.compile(r'\((.*?)\)\s+(.*?);')
    cpt_table_pattern = re.compile(r'table\s+(.*?);')
    cpt = {}

    # print("Parsing CPT for states:", states)  # Debugging output

    for line in cpt_lines:
        # print("CPT line:", line)  # Debugging output

        if cpt_value_match := cpt_value_pattern.match(line):
            state_values, probabilities = cpt_value_match.groups()
            state_values = state_values.replace('(', '').replace(')', '').split(', ')
            probabilities = list(map(float, probabilities.split(', ')))
            
            # print("State values:", state_values, "Probabilities:", probabilities)  # Debugging output
            
            # Ensure the probabilities match the number of states
            if len(probabilities) != len(states):
                raise ValueError("The number of probabilities does not match the number of states.")
            
            # Map the probabilities to corresponding states
            for state, prob in zip(states, probabilities):
                cpt[tuple(state_values) + (state,)] = prob
        elif cpt_table_match := cpt_table_pattern.match(line):
            probabilities = list(map(float, cpt_table_match.group(1).split(', ')))
            
            # print("Probabilities:", probabilities)  # Debugging output
            
            if len(probabilities) != len(states):
                raise ValueError("The number of probabilities does not match the number of states.")
            
            # Since there are no parent states, use a single tuple as the key
            for state, prob in zip(states, probabilities):
                cpt[(state,)] = prob

    if not cpt:
        print("Warning: CPT is empty after parsing.")  # Debugging output

    # print(cpt)
    # print()
    return cpt

def parse_bif(file_path):
    network = BayesianNetwork()
    current_variable_name = ""
    parsing_cpt = False
    cpt_lines = []

    var_pattern = re.compile(r'variable\s+(\w+)\s+\{')
    type_pattern = re.compile(r'type\s+discrete\s+\[\s*(\d+)\s*\]\s*\{(.*)\};')
    prob_pattern = re.compile(r'probability\s+\(\s*(\w+)(\s*\|\s*(.+?))?\s*\)\s+\{')
    cpt_value_pattern = re.compile(r'\((.*?)\)\s+(.*?);')
    cpt_table_pattern = re.compile(r'table\s+(.*?);')

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if var_match := var_pattern.match(line):
                current_variable_name = var_match.group(1)
                network.add_node(Node(current_variable_name, {}))

            elif type_match := type_pattern.match(line):
                _, state_values = type_match.groups()
                state_values = state_values.replace(',', '').split()
                network.get_node(current_variable_name).states = state_values

            elif prob_match := prob_pattern.match(line):
                variable_name = prob_match.group(1)
                given_vars = prob_match.group(3)
                if given_vars:
                    parents = given_vars.split(', ')
                    for parent in parents:
                        network.add_edge(parent.strip(), variable_name.strip())
                parsing_cpt = True
                cpt_lines = []

            elif parsing_cpt:
                if line == "}":
                    parsing_cpt = False
                    node = network.get_node(variable_name)
                    if not node:
                        raise ValueError(f"Node {variable_name} not found in network.")
                    node.cpt = parse_cpt(cpt_lines, node.states)
                else:
                    cpt_lines.append(line)

    return network

# if __name__ == "__main__":
#     # Get the current script's directory
#     current_dir = os.path.dirname(os.path.abspath(__file__))
    
#     # Construct the path to the .bif file
#     bif_path = os.path.join(current_dir, 'data', 'child.bif')

#     # Parse the .bif file and create a Bayesian Network
#     bayesian_network = parse_bif(bif_path)

#     # Print the resulting Bayesian Network
#     # bayesian_network.print_details()
#     # print(bayesian_network)
#     # bayesian_network.print_network()


#     query_node = 'Disease'

#     evidence = {
#         'LowerBodyO2': '<5',
#         'RUQO2': '>=12',
#         'CO2Report': '>=7.5',
#         'XrayReport': 'Asy/Patchy'
#     }


#     # Perform the query using the variable elimination method
#     # We need to catch errors in case the node names or evidence do not match the actual network structure
#     try:
#         result_factor = bayesian_network.variable_elimination(query=[query_node], evidence=evidence)
        
#         # Print the query results
#         print(f"Query result for the state of {query_node} given the evidence:")
#         for state, prob in result_factor.cpt.items():
#             print(f"State {state} has a probability of {prob:.4f}")
#     except ValueError as e:
#         print(str(e))
#     except KeyError as e:
#         print(f"Node or state not found: {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

