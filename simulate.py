#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

pi = numpy.pi
amplitude_BackLeg = pi/4
frequency_BackLeg = 10
phaseOffset_BackLeg = pi/8

amplitude_FrontLeg = pi/4
frequency_FrontLeg = 10
phaseOffset_FrontLeg = 0

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

#backLeg sensor vector
backLegSensorValues = numpy.zeros(1000)

#frontLeg sensor vector
frontLegSensorValues = numpy.zeros(1000)

#targetAngles vector
targetAngles_BackLeg = numpy.zeros(1000)
targetAngles_BackLeg = amplitude_BackLeg*numpy.sin(frequency_BackLeg * numpy.linspace(0,2*pi,1000) + phaseOffset_BackLeg)
targetAngles_FrontLeg = numpy.zeros(1000)
targetAngles_FrontLeg = amplitude_FrontLeg*numpy.sin(frequency_FrontLeg * numpy.linspace(0,2*pi,1000) + phaseOffset_FrontLeg)

#Save sensor and motor data to file
#numpy.save("data\\backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data\\frontLegSensorValues.npy", frontLegSensorValues)
#numpy.save("data\\targetAnglesBackLeg.npy",targetAngles_BackLeg)
#numpy.save("data\\targetAnglesFrontLeg.npy",targetAngles_FrontLeg)
#exit()

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
                                targetPosition= targetAngles_BackLeg[i],
                                maxForce = 15)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= "Torso_FrontLeg",
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= targetAngles_FrontLeg[i],
                                maxForce = 15)
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(1/60)
    
p.disconnect()




