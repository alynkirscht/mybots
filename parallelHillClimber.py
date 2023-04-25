from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import csv
import time

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        
        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessMatrix = numpy.zeros(shape=(c.populationSize, c.numberOfGenerations))

        for i in range(0, c.populationSize):
            self.parents[i]= SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration + 1)
            
                
            
    def Evolve_For_One_Generation(self, currentGeneration):
        
        self.Spawn()
    
        self.Mutate()
        
        self.Evaluate(self.children)
    
        self.Print()
        
        self.Select()

        self.Store_Fitness(currentGeneration)        
    
    def Spawn(self):
        self.children = {}

        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.nextAvailableID += 1
           
    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if (self.parents[i].fitness > self.children[i].fitness):
                self.parents[i] = self.children[i]

    def Store_Fitness(self, currentGeneration):
        population = 0
        for key in self.parents:
            sol = self.parents[key]
            self.fitnessMatrix[population][currentGeneration-1] = sol.fitness
            population += 1

    def Print(self):
        print("")
        for i in self.parents:
            print(self.parents[i].fitness, self.children[i].fitness)
            fitness = self.parents[i].fitness
            with open('data\\n3_brainiac.csv', 'a', newline='') as file:
                writer = csv.writer(file)

                writer.writerow(self.parents[i].normalAxis)
                writer.writerow([fitness])
                file.close()
        print("")


        
    def Show_Best(self):
        bestFitness = self.parents[0].fitness
        bestFitnessID = 0

        for i in range(len(self.parents)-1):
            if (bestFitness > self.parents[i+1].fitness):
                bestFitness = self.parents[i+1].fitness
                bestFitnessID = i+1    
                    
        # Save best angle values
        with open('data\\bestnseg_braniac.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(self.parents[bestFitnessID].normalAxis)
            writer.writerow([bestFitness])

            
            file.close()
        
        self.parents[bestFitnessID].Start_Simulation("GUI")

        if(c.numHiddenNeurons == 0):
            currentlyTesting = "A" 
        elif(c.numHiddenNeurons > 0):
            currentlyTesting = "B"
        numpy.savetxt("matrix" + currentlyTesting + ".csv", self.fitnessMatrix, delimiter =', ')
        numpy.save("matrix" + currentlyTesting + ".npy", self.fitnessMatrix)

        

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
            

