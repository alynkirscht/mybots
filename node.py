import random
import numpy
from connections import CONNECTIONS
class NODE:
    def __init__(self, id, size, RL, neurons, node_pos, joint_pos, node_orientation, joint_axis, scale):
        # Link 
        self.node_ID = id
        self.part_dimensions = size
    
        # Joint     
        self.joint_type = "revolute"
        self.set_Joint_Axis()

        # Recursive limit 
        self.recursive_limit = RL

        # Neurons     
        self.neurons = "" # I have no idea 

        # Connections 
        #self.connections = CONNECTIONS(node_pos, joint_pos, node_orientation, scale) 
       
    def set_Joint_Axis(self):
        self.joint_axis = numpy.zeros(3)
        while numpy.all(self.joint_axis == 0):
            self.joint_axis = numpy.random.randint(2, size=3)

node = NODE(0, [1,1,1], 1, "", [0,0,0],[0,0,0],[0,0,0], [0,0,0], 3)

    