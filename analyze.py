#Alyn Kirsch Tornell
#This program plots data collected by sensors

import numpy
import matplotlib.pyplot

#Get sensor data from file
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

#Get oscillation data from file
targetAngles_BackLeg = numpy.load("data/targetAnglesBackLeg.npy")
targetAngles_FrontLeg = numpy.load("data/targetAnglesFrontLeg.npy")

'''
#Plot analyzed data
matplotlib.pyplot.plot(backLegSensorValues, label= "Back Leg", linewidth= 2 )
matplotlib.pyplot.plot(frontLegSensorValues, label= "Front Leg", linewidth= 1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
'''
matplotlib.pyplot.plot(targetAngles_BackLeg, label = "backLeg targetAngles",
                       linewidth = 2)
matplotlib.pyplot.plot(targetAngles_FrontLeg, label = "frontLeg targetAngles",
                       linewidth = 1)
matplotlib.pyplot.title("Motor Commands")
matplotlib.pyplot.ylabel("Value in radians")
matplotlib.pyplot.xlabel("Steps")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
