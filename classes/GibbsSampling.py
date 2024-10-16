import random
from classes.BN import BN
from classes.Digraph import Digraph

class GibbsSampling:
    def __init__(self):
        pass


def containsEveryItem(target_string, items_list):
    # Convert the target_string to lowercase (optional, you can remove this if case sensitivity is desired)
    target_string = target_string.lower()

    # Iterate through the items in the list
    for item in items_list:
        # Convert the item to lowercase (optional)
        item = item.lower()

        # Check if the item is not in the target string
        if item not in target_string:
            return False

    # If we reach this point, all items were found in the target string
    return True

'''returns the string of the lhs's next state given the other states's current states'''
def calculateProbability(graph, lhs, currentValues):
    #first case, the probability is independent
    for factor in graph.facSet:
        if factor.getLHS() == lhs.label:
            #print(factor.getFactor())
            if factor.getRHS() is not None:
                #print(factor.getRHS())
                #get current states for each factor
                currentStates = []
                for f in factor.getRHS():
                    currentStates.append(currentValues[graph.getNode(f)])
                #print("currentStates:",currentStates)
                #get the correct table for lhs given the current states
                for row in factor.table:
                    if containsEveryItem(row[:][0], currentStates):
                        #print("row[0]:",row)
                        #print("row",row)
                        weights1 = []
                        for item in row[1:]:    #skips first element bc thats just identifer string
                            weights1.append(item)
                            #print("weights1",weights1)
                        chosenItem = random.choices(weights1,weights1, k=1)#chooses a probability of the list based
                                                                           #off of the probabilitites in the list...
                        #print(chosenItem[0])
                        index = weights1.index(chosenItem[0])   #index 0 bc k=1 so it stores one value in a list
                        return lhs.choices[index]

                #randomly choose new state from the probabilities given from correct table

            #if there is only the one variable with probabilities:
            else:
                weights = []
                for item in factor.table[0]:    #make a list of the probabilities from the table
                    weights.append(item)
                #print(factor.table)
                table = factor.table[0]     #just removes the only list out of another list
                chosenItem = random.choices(table, weights, k=1) #chooses from list according to probabilities
                #print(chosenItem[0])
                index = table.index(chosenItem[0])  #since index corresponds to the choices, get index to dictate state
                return lhs.choices[index]   #return state

                #return random.choice(factor)
def gibbsSampling(graph:Digraph, query, evidence, numberOfLoops, burnIn ):
    #currentstateVariable
    order = graph.getNodeSet()
    random.shuffle(order)

    #stores the current state of each node
    currentValues = {}

    #creates dictionary of every variable with a value of zero
    numberOfVariableVisits = {}
    for node in order:
        #create dictionary of possible states in a variable, the 0 is to count how many times
        #they occur
        nestedDictionary = {}
        for n in node.choices:
            nestedDictionary[str(n)] = 0
        #print("nested",nestedDictionary)
        numberOfVariableVisits[node.label] = nestedDictionary
        if node.label in evidence.keys():
             currentValues[node] = str(evidence[node.label])
        else:
            currentValues[node] = random.choice(node.getChoices())#randomly chooses a state for each var
    # print(numberOfVariableVisits)
    # print()
    # print(currentValues)
    # print()

    #print(calculateProbability(graph, order[0], currentValues))

    for i in range(numberOfLoops+1):
        for node in order:
            if node.label in evidence:
                pass
            else:
                choice = calculateProbability(graph, node, currentValues)
                currentValues[node] = str(choice) #updates new current state

                if i > burnIn:
                    #print("node:",node)
                    numberOfVariableVisits[node.label][str(currentValues[node])] += 1

    distribution = []
    print(query)
    for key, value in numberOfVariableVisits[query].items():
        val = round(value/(numberOfLoops-burnIn),5)
        distribution.append(val)
        print(key, ":", val)


