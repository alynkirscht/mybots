import random
import numpy
from connections import CONNECTIONS
import pyrosim
class NODE:
    def __init__(self, size, RL, neurons, root_node_pos, root_joint_pos, node_pos, joint_pos, node_orientation, scale):
        # Link 
        self.node_ID = 0
        self.part_dimensions = size
        self.node_position = root_node_pos
    
        # Joint     
        self.joint_type = "revolute"
        self.set_Joint_Axis()
        self.joint_position = root_joint_pos

        # Recursive limit 
        self.recursive_limit = RL

        # Neurons     
        self.neurons = neurons # I have no idea 

        # Connections 
        self.conn = CONNECTIONS(node_pos, joint_pos, node_orientation, scale, 0)

        self.create_links() 
       
    def set_Joint_Axis(self):
        self.joint_axis = numpy.zeros(3)
        while numpy.all(self.joint_axis == 0):
            self.joint_axis = numpy.random.randint(2, size=3)
    
    def create_Links(self):
        if (self.recursive_limit == 0):
            return
        # If it hasn't reached the recursive limit
        if (self.recursive_limit > 0): 
            pyrosim.Send_Cube( name="s" + str(self.node_ID), pos=self.conn.node_pos,size=self.part_dimensions)
            # If it's not the last link
            if (self.conn.terminal_only == 0):
                pyrosim.Send_Joint( name = "s" + str(self.node_ID) + "_s" + str(self.node_ID + 1),
                                    parent = "s" + str(self.node_ID), child = "s" + str(self.node_ID + 1),
                                    type = self.joint_type, position = self.conn.joint_pos, 
                                    jointAxis=self.joint_axis)
            
            self.update_Variables()
            self.create_Links()

    def update_Variables(self):
            #Link
            self.node_ID += 1
            self.part_dimensions *= self.conn.scale
            self.node_position = self.conn.node_pos

            # Joint
            self.set_Joint_Axis()
            self.joint_position = self.conn.joint_pos

            # Recurisve limit
            self.recursive_limit -= 1

            # Neurons
            self.neurons = "no idea"

            # Terminal only flag (Recursive limit reaches one before last)
            if (self.recursive_limit == 2):
                self.conn.terminal_only == 1
            
            
    