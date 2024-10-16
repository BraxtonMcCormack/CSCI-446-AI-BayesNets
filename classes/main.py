from classes.BIFParser import parse
from classes.Digraph import Digraph
from classes.Digraph import Node
import os

from classes.GibbsSampling import gibbsSampling

def main(BIF, query, evidence):
    path = os.path.join(os.curdir, "..", "data", BIF) #just gets the path to the BIFs
    '''Builds graph with nodes (arcs not included)'''
    graph = parse(path) #parses and returns Directional graph without arcs

    '''Creates arcs between nodes in the graph'''
    #formats factor names and add edges
    for f in graph.facSet:                             #for every factor in the set,
        string = f.getFactor()                      #assign the name to a string
        if "|" in string:                           #if there is a "given" symbol,
            rawList = string.split("|")             #split by the 'given' symbol
            l = []
            for segment in rawList:                 #removes extra characters
                segment = segment.replace("(", "")
                segment = segment.replace(")", "")
                segment = segment.strip()
                l.append(segment) #["destination", "source1 source2 ... sourceN"]
            #adding connections to adjacencyList (digraph)
            sources = l[1].split()  #separates all the sources into list
            destination = l[0]              #single destination
            f.setLHS(destination)
            f.setRHS(sources)
            d = graph.getNode(destination)  #retrieves the node from nodeList in graph object
            for source in sources:
                s = graph.getNode(source)
                graph.connect(s,d)

    numberOfLoops = 20000
    burnIn = 1000

    gibbsSampling(graph, query,evidence, numberOfLoops, burnIn)

def alarmTest():
    alarmQ = ['HYPOVOLEMIA', 'LVFAILURE', 'ERRLOWOUTPUT']
    alarmE1 = {
        'HRBP': 'HIGH',
        'CO': 'LOW',
        'BP': 'HIGH'
    }
    alarmE2 = {
        'HRBP': 'HIGH',
        'CO': 'LOW',
        'BP': 'HIGH',
        'HRSAT': 'LOW',
        'HREKG': 'LOW',
        'HISTORY': 'TRUE'
    }
    alarmEvidence = [alarmE1, alarmE2]

    # for q in alarmQ:
    #     count=0
    #     for evidence in alarmEvidence:
    #         count+=1
    #         print(q, "with evidence", count)
    #         main("alarm.bif", q, evidence)
    #         print(".............................")
    noEvidence = { }
    for i in alarmQ:
        main("alarm.bif", i, noEvidence)

def childTest():
    childQ = ['Disease']
    childE1 = {
        'LowerBodyO2': '<5',
        'RUQO2': '>=12',
        'CO2Report': '>=7.5',
        'XrayReport': 'Asy/Patchy'
    }

    childEvidence = [childE1]

    for q in childQ:
        count=0
        for evidence in childEvidence:
            count +=1
            print(q,"with evidence", count)
            main("child.bif", q, evidence)
            print(".............................")
    #
    # noEvidence = { }
    # for i in childQ:
    #     main("child.bif", i, noEvidence)
def hfTest():
    hfQ = ['SatContMoist', 'LLIW']
    # hfE1 = {
    #     'RSFcst': 'XNIL',
    #     'N32StarFcst': 'XNIL',
    #     'MountainFcst': 'XNIL',
    #     'AreaMoDryAir': 'VeryWet'
    # }
    hfE2 = {
        'RSFcst': 'XNIL',
        'N32StarFcst': 'XNIL',
        'MountainFcst': 'XNIL',
        'AreaMoDryAir': 'VeryWet',
        'CombVerMo': 'Down',
        'AreaMeso_ALS': 'Down',
        'CurPropConv': 'Strong'
    }
    hfEvidence = [hfE2]

    for q in hfQ:
        count=0
        for evidence in hfEvidence:
            count+=1
            print(q,"with evidence", count)
            main("hailfinder.bif", q, evidence)
            print(".............................")
    # noEvidence = { }
    # for i in hfQ:
    #     main("hailfinder.bif", i, noEvidence)
def insuranceTest():
    insuranceQ = ['MedCost', 'ILiCost', 'PropCost']
    # insuranceE1 = {
    #     'Age': 'Adolescent',
    #     'GoodStudent': 'False',
    #     'SeniorTrain': 'False',
    #     'DrivQuality': 'Poor'
    # }
    insuranceE2 = {
        'Age': 'Adolescent',
        'GoodStudent': 'False',
        'SeniorTrain': 'False',
        'DrivQuality': 'Poor',
        'MakeModel': 'Luxury',
        'DrivHistory': 'Zero'
    }
    insuranceEvidence = [insuranceE2]

    for q in insuranceQ:
        count = 0
        for evidence in insuranceEvidence:
            count+=1
            print(q,"with evidence", count)
            main("insurance.bif", q, evidence)
            print(".............................")

    # noEvidence = { }
    # for i in insuranceEvidence:
    #     main("insurance.bif", i, noEvidence)

def winTest():
    winQ = ['Problem1', 'Problem2', 'Problem3', 'Problem4', 'Problem5', 'Problem6']
    winE1 = {
        'Problem1': 'No_Output'
    }
    winE2 = {
        'Problem2': 'Too_Long'
    }
    winE3 = {
        'Problem3': 'No'
    }
    winE4 = {
        'Problem4': 'No'
    }
    winE5 = {
        'Problem5': 'No'
    }
    winE6 = {
        'Problem6': 'Yes'
    }
    winEvidence = [winE1]#, winE2, winE3, winE4, winE5, winE6]

    for q in winQ:
        count =0
        for evidence in winEvidence:
            count+=1
            print(q,"with evidence", count)
            main("win95pts.bif", q, evidence)
            print(".............................")
    # noEvidence = { }
    # for i in winQ:
    #     main("win95pts.bif", i, noEvidence)


print("Alarm==============================")
alarmTest() #No evidence
print("Child==============================")
childTest() #small evidence
print("Hailfinder==============================")
hfTest()
print("insurance==============================")
insuranceTest()
print("Win95pts==============================")
winTest()

