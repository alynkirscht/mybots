import pyrosim
import networkx as nx
class CONNECTIONS:

    def __init__(self, graph, id, scale, link_pos, joint_pos, TO):
        self.graph = graph
        self.snake_connection(id, scale, link_pos, joint_pos, TO)

    
    def snake_connection(self, id, scale, link_pos, joint_pos, TO):
        self.link_ID = id
        self.link_pos = link_pos
        self.joint_pos = joint_pos
        self.scale = scale
        self.terminal_only = TO

        self.add_Edge()

    def add_Edge(self):
        self.graph.add_edge( self.link_ID, self.link_ID + 1, link_position = self.link_pos, joint_position = self.joint_pos, 
                             scale = self.scale, terminal = self.terminal_only)
        