'''In instance of a variable or 'node'. the name is just the title of the var and the choices are the possible states it holds.
example: self.name = age, self.choices = ['young', 'middle', 'old']'''
class Variable:
    def __init__(self, name, nChoices, choices):
        self.name = name
        self.nChoices = nChoices
        self.choices = choices
    # Getter method for the 'name' attribute
    def getName(self):
        return self.name
    # Getter method for the 'nChoices' attribute
    def getNChoices(self):
        return self.nChoices
    # Getter method for the 'choices' attribute
    def getChoices(self):
        return self.choices
    def __str__(self):
        return self.name + ":" + str(self.choices)
