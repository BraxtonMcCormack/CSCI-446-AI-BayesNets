'''varSet is the set of all variables (the class) aka nodes,
   facSet is the set of all factors (the class) aka directional arcs
   ignore paramcount atm its not super necessary and doesnt do anything rn'''

class BN:
    def __init__(self):
        self.varSet = []
        self.facSet = []
        self.paramCount = None
    def addVar(self, var):
        self.varSet.append(var)
    def addFac(self, fac):
        self.facSet.append(fac)
    def setParamCount(self, n):
        self.paramCount = n
    def getVarSet(self):
        return self.varSet
    def getFacSet(self):
        return self.facSet

    def __str__(self):
        s = "variable count: "+str(len(self.varSet))
        s += "\n Parameter count: "+str(self.paramCount)
        return s
