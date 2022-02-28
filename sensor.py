import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    
    def __init__(self, linkName):
        self.linkName = linkName
        #Sensor vector
        self.values = numpy.zeros(c.REPETITIONS)
    
    def Get_Value(self, linkName, t):
        #Get value of sensors
        #print(self.values[self.t])
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)
        if (t == c.REPETITIONS-1):
            print(self.values)
        
       
