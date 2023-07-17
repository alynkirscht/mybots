from subprocess import Popen, PIPE
import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import sys
import time
import constants as c
from node import NODE
from connections import CONNECTIONS
import networkx as nx
import matplotlib.pyplot as plt

class SOLUTION:
    def __init__(self, nextAvailableID):
        

        """Recursion variables """
        self.recursive_limit = random.randint(3,5)
        self.num_links = self.recursive_limit # Starting recursive number
        self.numSensorNeurons = self.num_links
        self.numHiddenNeurons = c.numHiddenNeurons
        self.numMotorNeurons = self.num_links - 1

        self.sensorToHidden = numpy.random.random((self.numSensorNeurons,self.numHiddenNeurons))
        self.hiddenToMotor = numpy.random.random((self.numHiddenNeurons,self.numMotorNeurons))

        self.sensorToHidden = self.sensorToHidden * 2 - 1
        self.hiddenToMotor = self.hiddenToMotor * 2 - 1
    
        self.myID = nextAvailableID
        
       
        
    def Create_World(self):
        
        pyrosim.Start_SDF("world.sdf")

        # pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[2, 1, 1])

        pyrosim.End()

    def Create_Body(self):
        """This is Karl Sims new"""
        # Create body file 
        if (self.recursive_limit == self.num_links): 
            pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
            # Create graph 
            G = nx.Graph()
            self.terminal_only = 0
        
        # Recursive method
        if (self.recursive_limit == 0):
            pyrosim.End()
            self.recursive_limit = self.num_links
            return

        # If it hasn't reached the recursive limit
        if (self.recursive_limit > 0):
            # Terminal flag (one before last)
            if (self.recursive_limit == 1):
                self.terminal_only = 1

            # Root node case
            if (self.recursive_limit == self.num_links):
                # Initialize node class
                self.node = NODE(G, self.recursive_limit)
                #Set connection
                current_link = self.node.link_ID
                scale = [1,1,1] # no change
                link_pos = [0,.5,-.5] # no change
                joint_pos = [0,.5,-.5] # no change
                # terminal_only
                
                self.connection = CONNECTIONS(G,current_link, scale, link_pos, joint_pos, self.terminal_only)
                self.recursive_limit -= 1

            # Normal case 
            else: 
                self.node.snake_node(scale=self.connection.scale, joint_pos=self.connection.joint_pos, link_pos=self.connection.link_pos)
                #Set connection
                # self.node.link_ID
                scale = [1,1,1] # no change
                link_pos = [0,0,0] # no change
                joint_pos = [0,0,0] # no change
                self.connection.snake_connection(id=self.node.link_ID, scale=scale,link_pos=link_pos, joint_pos=joint_pos, TO=self.terminal_only)
                # Update recursive limit
                self.recursive_limit = self.node.recursive_limit
           
            pyrosim.Send_Cube( name="s" + str(self.node.link_ID), pos=self.node.link_position,size=self.node.link_size)
            
            # When it's not terminal
            if self.connection.terminal_only == 0:
                pyrosim.Send_Joint( name= 's' + str(self.node.link_ID) + '_' + 's' + str(self.node.link_ID + 1), 
                                    parent= 's' + str(self.node.link_ID), child= 's' + str(self.node.link_ID + 1),
                                    type= self.node.joint_type, position=self.node.joint_position, jointAxis=self.node.joint_axis)
            
            

            # RECURSIVE CALL
            self.Create_Body()
                    

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
        pass
        '''
        # random size or joint
        sizeOrJoint = random.randint(0,1)
        if sizeOrJoint == 0:
            # increase or decrease snake
            incOrDecSize = random.randint(0,1)
            # change size
            #increase size of snake if size is 3 or rand variable is 0 and size is 4
            if (self.recursive_limit == 3 or (self.recursive_limit == 4 and incOrDecSize == 0)):    
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

            randomJoint = random.randint(0, self.num_links - 2)
            randomCol = random.randint(0, 2)
            if self.normalAxis[randomJoint, randomCol] == 0:
                self.normalAxis[randomJoint, randomCol] = 1
            elif self.normalAxis[randomJoint, randomCol] == 1:
                row = self.normalAxis[randomJoint]
                if numpy.count_nonzero(row) == 1 and row[randomCol] == 1:
                    pass
                else:
                    self.normalAxis[randomJoint, randomCol] = 0'''

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