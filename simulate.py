#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim

#Create objects that handles physics and draws results to GUI
physicsClient = p.connect(p.GUI)

#Create normal force generated when hitting floor
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Add force of gravity
p.setGravity(0,0,-9.8)

#Add floor
planeId = p.loadURDF("plane.urdf")

#Add robot
robotId = p.loadURDF("body.urdf")

#Reads in the world described in world.sdf
p.loadSDF("world.sdf")

#Set up sensors
pyrosim.Prepare_To_Simulate(robotId)

#The for loop is used to slow things down
for i in range(1000):
    #Steps physics inside the world
    p.stepSimulation()
    #Add sensor to BackLeg link
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(1/60)
    print (i)
p.disconnect()
