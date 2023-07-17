import numpy
import networkx as nx
class NODE:
    def __init__(self, graph, RL):
        # Graph
        self.graph = graph
        # Link 
        self.link_ID = 0
        self.link_size = [1,1,1]
        self.link_position = [0,0,0.5]

        # Joint     
        self.joint_type = "revolute"
        self.joint_Axis()
        self.joint_position = [0, .5, .5]

        # Recursive limit 
        self.recursive_limit = RL

        # Connections
        self.connections = [self.link_ID + 1] # This formula changes depending on the shape

        self.add_Node()

    def snake_node(self, scale, joint_pos, link_pos):
        self.link_ID += 1
        self.link_size = [size * scale[i] for i, size in enumerate(self.link_size)] # [1,1,1] * [x,y,z]
        # Link position
        self.link_position = numpy.array(self.link_position)
        link_pos = numpy.array(link_pos)
        self.link_position = numpy.add(self.link_position, link_pos)
        self.link_position = self.link_position.tolist()

        # Joint position
        self.joint_position = numpy.array(self.joint_position)
        joint_pos = numpy.array(joint_pos)
        self.joint_position = numpy.add(self.joint_position, joint_pos)
        self.joint_position = self.joint_position.tolist()

        self.joint_axis = self.joint_Axis()
        self.recursive_limit -= 1
        self.connections = [self.link_ID + 1]  

        self.add_Node()


    def joint_Axis(self):
        self.joint_axis = numpy.zeros(3)
        while numpy.all(self.joint_axis == 0):
            self.joint_axis = numpy.random.randint(2, size=3)
            self.joint_axis = str(self.joint_axis).replace('[', '').replace(']', '')

        return self.joint_axis

    def add_Node(self):
        self.graph.add_node(self.link_ID, dimensions = self.link_size, recursive_limit = self.recursive_limit,
                    position = self.link_position, joint_position = self.joint_position, joint_axis = self.joint_axis, connections = self.connections)


    
       
