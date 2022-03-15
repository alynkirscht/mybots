from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self):
        #Add robot
        self.robotId = p.loadURDF("body.urdf")

        #Set up sensors
        pyrosim.Prepare_To_Simulate(self.robotId)

        #Activate sensors
        self.Prepare_To_Sense()

        #Activate motors
        self.Prepare_To_Act()


    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            #Create an instance of SENSOR class for each link
            self.sensors[linkName] = SENSOR(linkName)

        
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(i, t)

    def Think(self):
        pass


    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            #Create an instance of MOTOR class for each joint
            self.motors[jointName] = MOTOR(jointName)      


    def Act(self,t):
        for i in self.motors:
            self.motors[i].Set_Value(self.robotId, i, t)
        


        
