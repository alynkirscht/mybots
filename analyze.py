#Alyn Kirsch Tornell
#This program plots data collected by sensors

import numpy
import matplotlib.pyplot

#Get sensor data from file
backLegSensorValues = numpy.load("data/backLegSensorsValues.npy")

#Plot analyzed data
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()
