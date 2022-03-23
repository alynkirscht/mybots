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
        self.frequency = c.FREQUECY
        self.amplitude = c.AMPLITUDE
        self.offset = c.OFFSET
        if (self.jointName == "Torso_BackLeg"):
           self.offset = c.PI/8
        

    def Set_Value(self,robotId, desiredAngle):
        #self.motorValues[t] = self.amplitude * numpy.sin(self.frequency * t) + self.offset
        spacedArray = numpy.linspace(c.MIN_SIN,c.MAX_SIN,c.REPETITIONS)
        self.motorValues[desiredAngle] = self.amplitude * numpy.sin(self.frequency * spacedArray[desiredAngle]
                                                             + self.offset)
        #Add motor for joints
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName= self.jointName,
                                controlMode= p.POSITION_CONTROL,
                                targetPosition= self.motorValues[desiredAngle],
                                maxForce = c.MAX_FORCE)

    def Save_Values(self):
        numpy.save("data\\" + self.jointName + "SensorValues.npy", self.motorValues)
        
        
