import pybullet as p

class WORLD:
    def __init__(self):
        #Add floor
        self.planeId = p.loadURDF("plane.urdf")

        p.changeDynamics(self.planeId, -1, restitution=1)

        #Reads in the world described in world.sdf
        p.loadSDF("world.sdf")

