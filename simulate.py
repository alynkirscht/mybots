#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

#Create objects that handles physics and draws results to GUI
physicsClient = p.connect(p.GUI)

#Create normal force generated when hitting floor
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Add force of gravity
p.setGravity(0,0,c.GRAVITY)

#Add floor
planeId = p.loadURDF("plane.urdf")

#Add robot
robotId = p.loadURDF("body.urdf")

#Reads in the world described in world.sdf
p.loadSDF("world.sdf")

#Set up sensors
pyrosim.Prepare_To_Simulate(robotId)

#backLeg sensor vector
backLegSensorValues = numpy.zeros(c.REPETITIONS) #amplitude * sin(frequency x)

#frontLeg sensor vector
frontLegSensorValues = numpy.zeros(c.REPETITIONS)

#targetAngles vector
targetAngles_BackLeg = numpy.zeros(c.REPETITIONS)
targetAngles_BackLeg = c.AMPLITUDE_BACK_LEG*numpy.sin(c.FREQUECY_BACK_LEG
                                                   * numpy.linspace(c.MIN_SIN,c.MAX_SIN,
                                                                  c.REPETITIONS)
                                                      + c.PHASE_OFFSET_BACK_LEG)
targetAngles_FrontLeg = numpy.zeros(c.REPETITIONS)
targetAngles_FrontLeg = c.AMPLITUDE_FRONT_LEG*numpy.sin(c.FREQUECY_BACK_LEG
                                                     * numpy.linspace(c.MIN_SIN,c.MAX_SIN,
                                                                      c.REPETITIONS)
                                                     + c.PHASE_OFFSET_FRONT_LEG)

#Save sensor and motor data to file
#numpy.save("data\\backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data\\frontLegSensorValues.npy", frontLegSensorValues)
#numpy.save("data\\targetAnglesBackLeg.npy",targetAngles_BackLeg)
#numpy.save("data\\targetAnglesFrontLeg.npy",targetAngles_FrontLeg)
#exit()

#The for loop is used to slow things down
for i in range(c.REPETITIONS):
    #Steps physics inside the world
    p.stepSimulation()
    #Add sensor to BackLeg and FrontLeg links
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #Add motor for BackLeg and FrontLeg to torso joints
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= "Torso_BackLeg",
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= targetAngles_BackLeg[i],
                                maxForce = c.MAX_FORCE)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= "Torso_FrontLeg",
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= targetAngles_FrontLeg[i],
                                maxForce = c.MAX_FORCE)
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(c.SLEEP_TIME)
    
p.disconnect()




