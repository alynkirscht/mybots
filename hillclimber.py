from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()
            
    #Spawn a copy of self.parent
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        pass

    def Select(self):
        pass
            
