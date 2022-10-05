import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import numpy

class ROBOT:
    def __init__(self, solutionID):
        #Add robot
        self.robotId = p.loadURDF("body.urdf")

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
        print(self.sensors)

        
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
        
        for t in range(c.REPETITIONS):
            self.sensors['FrontLowerLeg'].Get_Value('FrontLowerLeg',t).Save_Values()
            self.sensors['LeftLowerLeg'].Get_Value('LeftLowerLeg',t).Save_Values()
            self.sensors['RightLowerLeg'].Get_Value('RightLowerLeg',t).Save_Values()
            self.sensors['BackLowerLeg'].Get_Value('BackLowerLeg',t).Save_Values()
            pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)
            for i in self.sensors:
                self.sensor_values = self.Sense(t)
            self.avg_sensors = numpy.array(self.sensor_values)
        file = open("tmp" + solutionID + ".txt", "w")
        file.write(str(self.avg_sensors))
        file.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" +
                  str(solutionID) + ".txt")
        """
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordindateOfLinkZero = positionOfLinkZero[0]
        file = open("tmp" + solutionID + ".txt", "w")
        file.write(str(xCoordindateOfLinkZero))
        file.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" +
                  str(solutionID) + ".txt")"""
