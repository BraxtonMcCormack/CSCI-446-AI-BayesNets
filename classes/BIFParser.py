from classes.BN import BN
from classes.Digraph import Digraph, Node
from classes.Factor import Factor
from classes.Variable import Variable

def parse(location):
    bn = BN()
    graph = Digraph()
    #reads bn
    f = open(location, 'r')
    name = ''
    l = []
    table = []
    readingTable = False
    for string in f:
        string = string.replace("\n","")
        string = string.replace(",", "")
        line = string.split()
        #print(line)
        #---------------------------------------------------------
        #if its a variable, do this
        if line[0]=='variable':
            name = line[1]
        #if type is first, that means its variable data
        elif line[0] == "type":
            start = line.index("{") + 1
            end = line.index("};")
            l = line[start:end]
            v = Variable(name, len(l), l)
            n = Node(name, l)
            bn.addVar(v)
            graph.addNode(n)
        #---------------------------------------------------------
        elif line[0] == "probability":
            start = string.index("(")
            end = string.index(")")+1
            name = string[start:end]
        elif string.strip()[0] == "(":
            if "REPEAT" in string:
                print("here")
            readingTable = True
            segment = []
            keys = string.lstrip()[:string.index(")")-1]
            vals = string.replace(";","").strip()[string.index(")"):].split()
            segment.append(keys)
            for v in vals:
                segment.append(float(v))
            table.append(segment)
        elif line[0] == "table":
            string = string.replace(";","")
            t= string.split()
            d= []
            for i in t:
                if i == "table":
                    pass
                else:
                    d.append(float(i))
            l = [d]
            bn.addFac(Factor(name, l))
            factor = Factor(name, l)
            splitName = name.split()
            factor.setLHS(splitName[1])
            graph.addFactor(factor)

        elif line[0] == "}":
            if readingTable:
                f = Factor(name, table)
                bn.addFac(f)
                graph.addFactor(f)
                table = []
            readingTable = False
            name = ''
    return graph
