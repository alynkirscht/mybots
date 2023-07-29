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
import csv
class SOLUTION:
    def __init__(self, nextAvailableID):
        

        """Recursion variables """
        self.recursive_limit = 4 # I am gonna choose 4 and then modify the snakes from there, random.randint(3,5)
        self.num_links = self.recursive_limit # Starting recursive number
        self.link_id = 0
        self.G = nx.Graph()
        self.Create_Graph()
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

    def Create_Graph(self):
        #Set terminal only flag
        self.terminal_only = 0
        # Recursive method
        if (self.recursive_limit == 0):            
            self.recursive_limit = self.num_links
            return

        # If it hasn't reached the recursive limit
        if (self.recursive_limit > 0):

            # Terminal flag (one before last)
            if (self.recursive_limit == 2):
                self.terminal_only = 1
                self.connections = [] 

            # Root node case
            if (self.recursive_limit == self.num_links):
                # Initialize node class
                self.node = NODE(self.G, self.recursive_limit, self.link_id)
                #Set connection
                scale = [1,1,1] # no change
                link_pos = [0,.5,-.5] # no change
                joint_pos = [0,.5,-.5] # no change
                # terminal_only
                self.connections = [self.link_id + 2]
                self.connection = CONNECTIONS(self.G,self.link_id, scale, link_pos, joint_pos, self.terminal_only, conns=self.connections.copy())
                self.recursive_limit -= 1
                self.link_id += 1

            # Normal case 
            else: 
                
                self.node.snake_node(id = self.link_id, RL=self.recursive_limit, scale=self.connection.scale, joint_pos=self.connection.joint_pos, link_pos=self.connection.link_pos, connections=self.connection.conns)
                scale = [1,1,1] # no change
                link_pos = [0,0,0] # no change
                joint_pos = [0,0,0] # no change
                #Set connection only if it's not last 
                if (self.terminal_only == 0):
                    self.connections = [self.link_id + 2]
                else:
                    self.connections.clear()
                if (self.connection.terminal_only == 0):    
                    self.connection.snake_connection(id=self.node.link_ID, scale=scale,link_pos=link_pos, joint_pos=joint_pos, TO=self.terminal_only, conns=self.connections)
                    
                # Update recursive limit
                # self.recursive_limit = self.node.recursive_limit
                self.recursive_limit -= 1  
                self.link_id += 1
  

        # RECURSIVE CALL
        self.Create_Graph()

    def Create_Body(self):
        for node, attributes in self.G.nodes(data=True):
            print(f"Node {node}: {attributes}")
        for edge in self.G.edges():
            node1, node2 = edge
            edge_data = self.G[node1][node2]
            print(f"Edge {edge}: {edge_data}")    
        """This is Karl Sims new"""
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        # Creat links from graph
        for node in self.G.nodes():
            pyrosim.Send_Cube( name="s" + str(node), pos=self.G.nodes[node]["position"],size=self.G.nodes[node]["dimensions"])

            # Create joints from graph (only if connections is filled)
            if (len(self.G.nodes[node]["connections"]) > 0):
                for edge in range(len(self.G.nodes[node]["connections"])):
                    pyrosim.Send_Joint( name= 's' + str(node) + '_' + 's' + str(self.G.nodes[node]["connections"][edge]), 
                                        parent= 's' + str(node), child= 's' + str(self.G.nodes[node]["connections"][edge]),
                                        type= "revolute", position=self.G.nodes[node]["joint_position"], jointAxis=self.G.nodes[node]["joint_axis"])               
    
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
        # Chooses mutation
        mutation = random.randint(0,4)
        
        # Change size of one link
        if mutation == 0:
            rand_link =  random.randint(0, self.num_links)
            rand_size = random.uniform(0.5, 1.5)
            self.G.nodes[rand_link]["dimensions"] = [ col * rand_size for col in self.G.nodes[rand_link]["dimensions"]]

            randomRowSToH = random.randint(0,self.numSensorNeurons-1)
            randomColumnSToH = random.randint(0,self.numHiddenNeurons-1)
            randomRowHToM = random.randint(0,self.numHiddenNeurons-1)
            randomColumnHToM = random.randint(0,self.numMotorNeurons-1)

            self.sensorToHidden[randomRowSToH, randomColumnSToH] = random.random() * 2 -1
            self.hiddenToMotor[randomRowHToM, randomColumnHToM] = random.random() * 2 -1       
        # Change normalAxis
        elif mutation == 1:
            rand_joint = random.randint(0, self.num_links - 1)
            rand_axis =  self.node.joint_Axis()
            self.G.nodes[rand_joint]["joint_axis"] = rand_axis

            randomRowSToH = random.randint(0,self.numSensorNeurons-1)
            randomColumnSToH = random.randint(0,self.numHiddenNeurons-1)
            randomRowHToM = random.randint(0,self.numHiddenNeurons-1)
            randomColumnHToM = random.randint(0,self.numMotorNeurons-1)

            self.sensorToHidden[randomRowSToH, randomColumnSToH] = random.random() * 2 -1
            self.hiddenToMotor[randomRowHToM, randomColumnHToM] = random.random() * 2 -1
        # Add link
        elif mutation == 2:
            self.terminal_only = 1

            scale = [1,1,1] # no change
            link_pos = [0,0,0] # no change
            joint_pos = [0,0,0] # no change

            self.G[self.num_links - 2][self.num_links - 1]["terminal"] = 0
            self.G.nodes[self.num_links - 1]["connections"] = [self.link_id]
            self.connections = []
            self.connection.snake_connection(self.num_links - 1, scale, link_pos, joint_pos, self.terminal_only, self.connections)
            self.node.snake_node(self.num_links, self.recursive_limit, self.connection.scale, self.connection.joint_pos, self.connection.link_pos, self.connection.conns)


            self.link_id += 1
            self.recursive_limit += 1
            self.num_links = self.recursive_limit

            # update neurons
            self.numSensorNeurons = self.num_links
            self.numMotorNeurons = self.num_links - 1

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
        elif mutation == 3: 
            # Remove last node and connection
            self.G.remove_node(self.num_links - 1)
            self.G.nodes[self.num_links - 2]["connections"] = []
            # self.G.remove_edge(self.num_links - 1, self.num_links - 2)
            

            self.link_id -= 1
            self.num_links -= 1
            self.recursive_limit = self.num_links
            
            # update neurons
            self.numSensorNeurons = self.num_links
            self.numMotorNeurons = self.num_links - 1

            
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