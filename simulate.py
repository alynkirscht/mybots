#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

pi = math.pi

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

#Numpy backLeg sensor vector
backLegSensorValues = numpy.zeros(1000)

#Numpy frontLeg sensor vector
frontLegSensorValues = numpy.zeros(1000)

#The for loop is used to slow things down
for i in range(1000):
    #Steps physics inside the world
    p.stepSimulation()
    #Add sensor to BackLeg and FrontLeg links
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #Add motor for BackLeg and FrontLeg to torso joints
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= "Torso_BackLeg",
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= random.uniform(-pi/2,pi/2),
                                maxForce = 35)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= "Torso_FrontLeg",
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= random.uniform(-pi/2,pi/2),
                                maxForce = 35)
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(1/60)
    print (i)
#Save sensor data to file
numpy.save("data\\backLegSensorValues.npy", backLegSensorValues)
numpy.save("data\\frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
