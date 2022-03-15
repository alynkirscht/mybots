import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        #Motor vector
        self.motorValues = numpy.zeros(c.REPETITIONS)

        #Motor vector values
        self.frequency = 1#c.FREQUECY_BACK_LEG
        self.amplitude = numpy.pi/4 #c.AMPLITUDE_BACK_LEG
        self.offset = 0#c.PHASE_OFFSET_FRONT_LEG

    def Set_Value(self,robotId, i,t):
        #self.motorValues[t] = self.amplitude * numpy.sin(self.frequency * t) + self.offset
        spacedArray = numpy.linspace(c.MIN_SIN,c.MAX_SIN,c.REPETITIONS)
        self.motorValues[t] = c.AMPLITUDE_BACK_LEG*numpy.sin(c.FREQUECY_BACK_LEG * spacedArray[t]
                                                             + c.PHASE_OFFSET_BACK_LEG)
        #Add motor for joints
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= self.jointName,
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= self.motorValues[t],
                                maxForce = c.MAX_FORCE)
        
        
