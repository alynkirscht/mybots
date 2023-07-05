from subprocess import Popen, PIPE
import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import sys
import time
import constants as c
from node import NODE

class SOLUTION:
    def __init__(self, nextAvailableID):
        

        """Here I would initialize node?"""
        self.recursive_limit = random.randint(3,5)
        self.root_node_pos = [0, 0, 0.5] 
        self.root_node_size = [1,1,1]
        self.node_ID = 0

        # Root node
        root_node = NODE( self.node_ID, self.root_node_size, self.recursive_limit, "neurons", 
                          self.root_node_pos, "node_orientation", "scale")

        self.node_ID += 1
        self.recursive_limit -= 1

        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        pyrosim.Send_Cube( name="s" + str(root_node.node_ID), pos=root_node.connections.node_pos,
                           size=root_node.part_dimensions)
        pyrosim.Send_Joint( name = "s" + str(root_node.node_ID) + "_s" + str(root_node.node_ID + 1),
                            parent = "s" + str(root_node.node_ID), child = "s" + str(root_node.node_ID + 1),
                            type = root_node.joint_type, position = root_node.connections.joint_pos, 
                            jointAxis=root_node.joint_axis)
         
        # randomize size of snake
        #size 6 links, 5 joints
        
        self.numLinksJoint =  random.randint(1, 3) #size ranges from 3 links to 5 links
        self.numSensorNeurons = self.numLinksJoint + 2
        self.numHiddenNeurons = c.numHiddenNeurons
        self.numMotorNeurons = self.numLinksJoint + 1

        self.sensorToHidden = numpy.random.random((self.numSensorNeurons,self.numHiddenNeurons))
        self.hiddenToMotor = numpy.random.random((self.numHiddenNeurons,self.numMotorNeurons))

        self.sensorToHidden = self.sensorToHidden * 2 - 1
        self.hiddenToMotor = self.hiddenToMotor * 2 - 1

        # array of arrays for the values of the normal axis with numLinksJoints + 1 num of rows and 3 num of columns
        # self.normalAxis = numpy.array([[1., 0., 0.],[0., 1., 1.],[1., 0., 0.],[0., 1., 0.],[1., 0., 1.]])
        
        self.normalAxis = numpy.zeros((self.numLinksJoint + 1, 3))
        for i in range(self.numLinksJoint + 1):
            row = numpy.zeros(3)
            while numpy.all(row == 0):
                row = numpy.random.randint(2, size=3)
            self.normalAxis[i] = row
    
        self.myID = nextAvailableID
        
       
        
    def Create_World(self):
        
        pyrosim.Start_SDF("world.sdf")

        # pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[2, 1, 1])

        pyrosim.End()

    def Create_Body(self):
        """This is Karl Sims new"""
        

        for linksJoint in range(self.numLinksJoint):
            # number of joints is 1 less than num joints
            if (linksJoint != self.numLinksJoint - 1):
                jointAxis = str(self.normalAxis[linksJoint]).replace('[', '').replace(']', '')
            pyrosim.Send_Cube(name='s' + str(linksJoint + 1), pos=[0, .5, 0], size=[1, 1, 1])
            
            pyrosim.Send_Joint( name = 's' + str(linksJoint + 1) + '_' + 's' + str(linksJoint + 2), parent = 's' + str(linksJoint + 1), child = 's' + str(linksJoint + 2),
                                type = "revolute", position = [0, 1 , 0], jointAxis=jointAxis)
              
        pyrosim.Send_Cube(name='s' + str(self.numLinksJoint + 1), pos=[0, .5, 0], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        for sensor in range(self.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = sensor, linkName = 's' + str(sensor))

        for hidden in range(self.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron( name = hidden + self.numSensorNeurons)
        
        for motor in range (self.numMotorNeurons): 
            pyrosim.Send_Motor_Neuron( name = (motor + self.numSensorNeurons + self.numHiddenNeurons) , jointName = 's' + str(motor) + '_' + 's' + str(motor + 1) )
        
        # sensor to hidden
        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numHiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow ,
                                     targetNeuronName = currentColumn + self.numSensorNeurons,
                                     weight = self.sensorToHidden[currentRow][currentColumn])
        
        # hidden to motor
        for currentRow in range(self.numHiddenNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow + self.numSensorNeurons,
                                    targetNeuronName = currentColumn + self.numSensorNeurons + self.numHiddenNeurons, 
                                    weight = self.hiddenToMotor[currentRow][currentColumn])
        
        pyrosim.End()


    def Mutate(self):
        

        # random size or joint
        sizeOrJoint = random.randint(0,1)
        if sizeOrJoint == 0:
            # increase or decrease snake
            incOrDecSize = random.randint(0,1)
            # change size
            #increase size of snake if size is 3 or rand variable is 0 and size is 4
            if (self.numLinksJoint == 1 or (self.numLinksJoint == 2 and incOrDecSize == 0)):    
                self.numLinksJoint += 1

                # add new row to normalAxis array
                new_row = numpy.zeros(3)
                while numpy.all(new_row == 0):
                    new_row = numpy.random.randint(2, size=3)
                self.normalAxis = numpy.vstack((self.normalAxis, new_row))

                # update neurons
                self.numSensorNeurons = self.numLinksJoint + 2
                self.numMotorNeurons = self.numLinksJoint + 1

                 # Increase size by 1 in both dimensions
                sensorToHidden = numpy.zeros((self.numSensorNeurons, self.numHiddenNeurons))
                sensorToHidden[:self.numSensorNeurons -1, :] = self.sensorToHidden

                hiddenToMotor = numpy.zeros((self.numHiddenNeurons, self.numMotorNeurons))
                hiddenToMotor[:, :self.numMotorNeurons -1] = self.hiddenToMotor

                # Append new values
                new_weight_row_sToH = numpy.random.random((1, self.numHiddenNeurons)) * 2 - 1
                sensorToHidden[-1, :] = new_weight_row_sToH
                new_weight_column_sToH = numpy.random.random((self.numSensorNeurons, 1)) * 2 - 1
                sensorToHidden[:, -1] = new_weight_column_sToH.flatten()

                new_weight_row_hToM = numpy.random.random((1, self.numMotorNeurons)) * 2 - 1
                hiddenToMotor[-1, :] = new_weight_row_hToM
                new_weight_column_hToM = numpy.random.random((self.numHiddenNeurons, 1)) * 2 - 1
                hiddenToMotor[:, -1] = new_weight_column_hToM.flatten()

                self.sensorToHidden = sensorToHidden
                self.hiddenToMotor = hiddenToMotor

            # decrease size if snake is of size 5 or rand variable is 1 and is of size 4
            elif (self.numLinksJoint == 3 or (self.numLinksJoint == 2 and incOrDecSize == 1)): 
                self.numLinksJoint -= 1

                # remove last row from normalAxis array
                self.normalAxis = self.normalAxis[:-1]
                
                # update neurons
                self.numSensorNeurons = self.numLinksJoint + 2
                self.numMotorNeurons = self.numLinksJoint + 1

               
                # Create the new array with the desired size
                sensorToHidden = numpy.zeros((self.numSensorNeurons, self.numHiddenNeurons))
                hiddenToMotor = numpy.zeros((self.numHiddenNeurons, self.numMotorNeurons))

                # Copy the values from the original array to the new array
                for i in range(self.numSensorNeurons):
                    for j in range(self.numHiddenNeurons):
                        sensorToHidden[i,j] = sensorToHidden[i,j]
                for i in range(self.numHiddenNeurons):
                    for j in range(self.numMotorNeurons):
                        hiddenToMotor[i,j] = hiddenToMotor[i,j]
                
                self.sensorToHidden = sensorToHidden
                self.hiddenToMotor = hiddenToMotor
            

        # change joint axis
        else:
            randomRowSToH = random.randint(0,self.numSensorNeurons-1)
            randomColumnSToH = random.randint(0,self.numHiddenNeurons-1)
            randomRowHToM = random.randint(0,self.numHiddenNeurons-1)
            randomColumnHToM = random.randint(0,self.numMotorNeurons-1)

            self.sensorToHidden[randomRowSToH, randomColumnSToH] = random.random() * 2 -1
            self.hiddenToMotor[randomRowHToM, randomColumnHToM] = random.random() * 2 -1

            randomJoint = random.randint(0, self.numLinksJoint)
            randomCol = random.randint(0, 2)
            if self.normalAxis[randomJoint, randomCol] == 0:
                self.normalAxis[randomJoint, randomCol] = 1
            elif self.normalAxis[randomJoint, randomCol] == 1:
                row = self.normalAxis[randomJoint]
                if numpy.count_nonzero(row) == 1 and row[randomCol] == 1:
                    pass
                else:
                    self.normalAxis[randomJoint, randomCol] = 0

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
        os.system("chomd 755 fitness" + str(self.myID) + ".txt")    
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        os.system("del fitness" + str(self.myID) + ".txt")