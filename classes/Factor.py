'''An instance of a factor or probability. 

var cool has 2 states, cool and NOTcool (order matters here)
var playsPKMN has 2 states playsPKMN and NOTplaysPKMN. where the probability of playsPKMN and NOT is arbitrary atm

example: self.factor = "( Cool | playsPokemon )" and 
self.table = 
[ ["playsPKMN", .6, .4], 
  ["NOTplaysPKMN", .4, .6] ]

the example is saying what is the probability of a person being cool, given they play pokemon is .6 or 60%. the .6 in the self.table[0][0]
corresponds to them being cool, and the .4 is under the column of NOTcool
  '''
class Factor:
    def __init__(self, factor, table):
        self.factor = factor
        self.table = table
        self.LHS = None
        self.RHS = None
    # Getter method for the 'factor' attribute
    def getFactor(self):
        return self.factor

    def setLHS(self, val):
        self.LHS = val
    def setRHS(self, val):
        self.RHS = val

    def getLHS(self):
        return self.LHS #string value
    def getRHS(self):
        return self.RHS #list value
    # Getter method for the 'table' attribute
    def getTable(self):
        return self.table
    def __str__(self):
        s = "factor:" + self.factor
        for row in self.table:
            s = s+"\n"+str(row)
        return s
