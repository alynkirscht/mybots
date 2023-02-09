import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import sys
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        # randomize size of snake
        self.numLinksJoint = random.randint(0, 10)
        self.numSensorNeurons = self.numLinksJoint + 2
        self.numMotorNeurons = self.numLinksJoint + 1

        self.weights = numpy.random.random((self.numSensorNeurons,self.numMotorNeurons))
       
        self.weights = self.weights * 2 -1

        self.myID = nextAvailableID

       
        
    def Create_World(self):
        
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        normalVector = self.Random_Normal_Vector()
        
        pyrosim.Send_Cube(name="s0", pos=[0,0,.5], size=[1, 1, 1])

        pyrosim.Send_Joint( name = "s0_s1", parent = "s0", child = "s1",
                            type = "revolute", position = [0, .5 , .5], jointAxis="1 0 0")
        
        for linksJoint in range(self.numLinksJoint):
            normalVector = self.Random_Normal_Vector()

            pyrosim.Send_Cube(name='s' + str(linksJoint + 1), pos=[0, .5, 0], size=[1, 1, 1])

            pyrosim.Send_Joint( name = 's' + str(linksJoint + 1) + '_' + 's' + str(linksJoint + 2), parent = 's' + str(linksJoint + 1), child = 's' + str(linksJoint + 2),
                                type = "revolute", position = [0, 1 , 0], jointAxis=normalVector)

        normalVector = self.Random_Normal_Vector()    
        pyrosim.Send_Cube(name='s' + str(self.numLinksJoint + 1), pos=[0, .5, 0], size=[1, 1, 1])

        pyrosim.End()
        

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        for sensor in range(self.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = sensor, linkName = 's' + str(sensor))
        
        for motor in range (self.numMotorNeurons): 
            pyrosim.Send_Motor_Neuron( name = (motor + self.numSensorNeurons) , jointName = 's' + str(motor) + '_' + 's' + str(motor + 1) )
        
        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow ,
                                     targetNeuronName = currentColumn + self.numSensorNeurons,
                                     weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,self.numSensorNeurons-1)
        randomColumn = random.randint(0,self.numMotorNeurons-1)

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
    
    def Random_Normal_Vector(self):
        # randomize normal vectors
        randomVector = random.randint(0,2)
        if randomVector == 0:
            normalVector = "1 0 0"
        elif randomVector == 1:
            normalVector = "0 1 0"
        elif randomVector == 2:
            normalVector = "0 0 1"

        return normalVector

    
                  
        
