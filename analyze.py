#Alyn Kirsch Tornell
#This program plots data collected by sensors

import numpy
import matplotlib.pyplot

#Get sensor data from file
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

#Plot analyzed data
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
