#Alyn Kirsch Tornell
#This program simulates the world robots will live in
from simulation import SIMULATION
import sys

print(sys.argv[0])
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()




