import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
from solution import SOLUTION
import networkx as nx


class ROBOT:
    def __init__(self, solutionID, restitution, num_links):
        #Add robot
        self.robotId = p.loadURDF("body" + solutionID + ".urdf")
        # Change the restitution of all links
        '''
        if restitution != 0:
            for link_index in range(int(num_links)):
                p.changeDynamics(self.robotId, linkIndex=link_index, restitution=float(restitution))
        #p.changeDynamics(self.robotId, linkIndex=int(num_links) - 1, restitution=float(restitution))
        '''
        
        self.z = []
        os.system("del body" + solutionID + ".urdf")

        #Set up sensors
        pyrosim.Prepare_To_Simulate(self.robotId)

        

        #Activate sensors
        self.Prepare_To_Sense()

        #Activate motors
        self.Prepare_To_Act()


        #Creates neural network
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")

        os.system("del brain" + solutionID + ".nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            #Create an instance of SENSOR class for each link
            self.sensors[linkName] = SENSOR(linkName)

        
    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(i, t)


    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            #Create an instance of MOTOR class for each joint
            self.motors[jointName] = MOTOR(jointName)      


    def Act(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self, solutionID):
        print("Solution ID: " + str(solutionID))
        print("Robot Id: " + str(self.robotId))
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        yPosition = basePosition[1]
        self.z.append(basePosition[2])

        fitness = yPosition + max(self.z)
    
        file = open("tmp" + solutionID + ".txt", "w")
        file.write(str(fitness))
        file.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" +
                  str(solutionID) + ".txt")


        
