import pybullet as p

class WORLD:
    def __init__(self):
        #Add floor
        self.planeId = p.loadURDF("plane.urdf")

        #Reads in the world described in world.sdf
        p.loadSDF("world.sdf")

