#Alyn Kirsch Tornell
#This program simulates the world robots will live in
from simulation import SIMULATION
import sys

print(sys.argv[0])
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
restitution = sys.argv[3]
num_links = sys.argv[4]
simulation = SIMULATION(directOrGUI, solutionID, restitution, num_links)
simulation.Run()
simulation.Get_Fitness()




