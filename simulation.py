import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        elif (directOrGUI == "GUI"):
            self.physicsClient = p.connect(p.GUI)
            
        #Create normal force generated when hitting floor
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #Add force of gravity
        p.setGravity(0,0,c.GRAVITY)
        
        self.solutionID = solutionID
        self.robot = ROBOT(self.solutionID)
        self.world = WORLD()

        self.directOrGUI = directOrGUI
        
    def __del__(self):
        p.disconnect()

    
    def Run(self):
        #The for loop is used to slow things down
        for i in range(c.REPETITIONS):
            
            #Steps physics inside the world
            p.stepSimulation()


            #Enable sensing in robot
            self.robot.Sense(i)

            #Enable thinking in the robot
            self.robot.Think()

            #Enable acting in robot
            self.robot.Act(i)

            if (self.directOrGUI == "GUI"):
                time.sleep(c.SLEEP_TIME) 
            
            #print(i)
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)
            

