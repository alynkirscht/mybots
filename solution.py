import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import sys
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.random((c.numSensorNeurons,c.numMotorNeurons))
       
        self.weights = self.weights * 2 -1

        self.myID = nextAvailableID
        
    def Create_World(self):
        
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name="s0", pos=[0,0,.5], size=[1, 1, 1])

        
        pyrosim.Send_Joint( name = "s0_s1", parent = "s0", child = "s1",
                            type = "revolute", position = [0, .5 , .5], jointAxis="0 0 1")
        
        pyrosim.Send_Cube(name="s1", pos=[0, .5, 0], size=[1, 1, 1])

        pyrosim.Send_Joint( name = "s1_s2", parent = "s1", child = "s2",
                            type = "revolute", position = [0, 1 , 0], jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="s2", pos=[0, .5, 0], size=[1, 1, 1])
        
        
        pyrosim.Send_Joint( name = "s2_s3", parent = "s2", child = "s3",
                            type = "revolute", position = [0, 1 , 0], jointAxis="0 0 1")
        
        pyrosim.Send_Cube(name="s3", pos=[0, .5, 0], size=[1, 1, 1])

        pyrosim.End()
        

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "s0")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "s1")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "s2")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "s3")
        
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "s0_s1")
        pyrosim.Send_Motor_Neuron( name = 5, jointName = "s1_s2")
        pyrosim.Send_Motor_Neuron( name = 6, jointName = "s2_s3")
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow ,
                                     targetNeuronName = currentColumn + c.numSensorNeurons ,
                                     weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)

        self.weights[randomRow, randomColumn] = random.random() * 2 -1

    def Set_ID(self):
        return self.myID + 1

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + str(directOrGUI) + " " + str(self.myID) )

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    
                  
        
