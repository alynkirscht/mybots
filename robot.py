import pybullet as p

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        #Add robot
        self.robotId = p.loadURDF("body.urdf")
