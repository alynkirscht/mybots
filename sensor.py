import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    
    def __init__(self, linkName):
        self.linkName = linkName
        #Sensor vector
        self.values = numpy.zeros(c.REPETITIONS)
    
    #Get value of sensors    
    def Get_Value(self, linkName, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)
    
    #Save sensor data to file
    def Save_Values():
        numpy.save("data\\" + self.linkName + "SensorValues.npy", self.values)
     
        
        
       
