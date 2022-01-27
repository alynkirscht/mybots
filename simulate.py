#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time

#Create objects that handles physics and draws results to GUI
physicsClient = p.connect(p.GUI)

#Reads in the world described in box.sdf
p.loadSDF("box.sdf")

#The for loop is used to slow thingd down
for i in range(1000):
    #Steps physics inside the world
    p.stepSimulation()
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(1/60)
    print (i)
p.disconnect()
