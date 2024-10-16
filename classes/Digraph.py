from classes.Factor import Factor


class Node:
    def __init__(self, label, choices):
        self.label = label
        self.children = []
        self.parents = []
        self.choices = choices
        self.nChoices = len(choices)
    def __str__(self):
        return self.label
    def getChoices(self):
        return self.choices
    def addChild(self, node):
        self.children.append(node)
    def addParent(self, node):
        self.parents.append(node)
    def getChildren(self):
        return self.children
    def getParents(self):
        return self.parents
    def markovBlanket(self):
        blanket = set()
        for parent in self.parents:
            blanket.add(parent)
        for child in self.children:
            blanket.add(child)
            for parent_of_child in child.parents:
                blanket.add(parent_of_child)
        # removes self from mb
        blanket.discard(self)
        # Convert the set to a list and return it
        #print(self.label+" markovBlanketSize:",len(list(blanket)))
        return list(blanket)


class Digraph:
    def __init__(self):
        self.nodeSet = []
        self.facSet = []
    def addNode(self, node):
        self.nodeSet.append(node)
    def addFactor(self, factor:Factor):
        self.facSet.append(factor)
    def __str__(self):

        s = ''
        for n in self.nodeSet:
            pstring= ''
            for i in n.getParents():
                pstring += str(i)+ " "
            cstring = ''
            for i in n.getChildren():
                cstring+= str(i)+ " "
            s += str(n)+"\n\tparents:"+pstring+ "\n"
            s += "\tchildren:"+cstring+"\n"
        return s
    def getNode(self, label):
        for node in self.nodeSet:
            if node.label == label:
                return node
        print("Node does not exist in list MAJOR ERROR")
    def connect(self, source, dest):
        source.children.append(dest)
        dest.parents.append(source)
    def getNodeSet(self):
        return self.nodeSet
    def averageMB(self):
        total = 0
        for node in self.nodeSet:
            total += len(node.markovBlanket())
        result = total/len(self.nodeSet)
        return round(result,2)



