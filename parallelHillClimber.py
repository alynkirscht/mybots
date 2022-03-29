from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(0, c.populationSize):
            self.parents[i]= SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation("DIRECT")

        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    def Evolve_For_One_Generation(self):
        pass
##        self.Spawn()
##    
##        self.Mutate()
##        
##        self.child.Evaluate("DIRECT")
##
##        self.Print()
##        
##        self.Select()
##            
    #Spawn a copy of self.parent
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.nextAvailableID = Set_ID()
        self.nextAvailableID += 1
        
    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        ''' self.parent.Evaluate("GUI")'''
        pass

