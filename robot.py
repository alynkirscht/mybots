import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import constants as c

class ROBOT:
    def __init__(self):
        self.motors = {}

        #Add robot
        self.robotId = p.loadURDF("body.urdf")

        #Set up sensors
        pyrosim.Prepare_To_Simulate(self.robotId)

        #Activate sensors
        self.Prepare_To_Sense()

        

    
    @classmethod
    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            #Create an instance of SENSOR class for each link
            self.sensors[linkName] = SENSOR(linkName)
        #print(self.sensors)

    @classmethod
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(i, t)


        
