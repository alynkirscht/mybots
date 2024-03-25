import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        
    def Set_Value(self,robotId, desiredAngle):
        #self.motorValues[t] = self.amplitude * numpy.sin(self.frequency * t) + self.offset
        spacedArray = numpy.linspace(c.MIN_SIN,c.MAX_SIN,c.REPETITIONS)
        '''self.motorValues[t] = self.amplitude * numpy.sin(self.frequency * spacedArray[t]
                                                             + self.offset)'''

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= self.jointName,
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= desiredAngle,
                                maxForce = c.MAX_FORCE)
