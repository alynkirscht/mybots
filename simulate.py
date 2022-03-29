#Alyn Kirsch Tornell
#This program simulates the world robots will live in
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()




