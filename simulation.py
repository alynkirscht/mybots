import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI) #handles physics and draws
                                              #results to GUI
        #Create normal force generated when hitting floor
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #Add force of gravity
        p.setGravity(0,0,c.GRAVITY) 

        self.robot = ROBOT()

        #Set up sensors
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
    
        self.world = WORLD()

    @classmethod
    def Run(cls):
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

            print(i)
        
        
    
    #p.disconnect()
