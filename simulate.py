#Alyn Kirsch Tornell
#This program simulates the world robots will live in
from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()
'''


import numpy
import random







#backLeg sensor vector
backLegSensorValues = numpy.zeros(c.REPETITIONS) #amplitude * sin(frequency x)

#frontLeg sensor vector
frontLegSensorValues = numpy.zeros(c.REPETITIONS)

#targetAngles vector
targetAngles_BackLeg = numpy.zeros(c.REPETITIONS)
targetAngles_BackLeg = c.AMPLITUDE_BACK_LEG*numpy.sin(c.FREQUECY_BACK_LEG
                                                   * numpy.linspace(c.MIN_SIN,c.MAX_SIN,
                                                                  c.REPETITIONS)
                                                      + c.PHASE_OFFSET_BACK_LEG)
targetAngles_FrontLeg = numpy.zeros(c.REPETITIONS)
targetAngles_FrontLeg = c.AMPLITUDE_FRONT_LEG*numpy.sin(c.FREQUECY_BACK_LEG
                                                     * numpy.linspace(c.MIN_SIN,c.MAX_SIN,
                                                                      c.REPETITIONS)
                                                     + c.PHASE_OFFSET_FRONT_LEG)

#Save sensor and motor data to file
#numpy.save("data\\backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data\\frontLegSensorValues.npy", frontLegSensorValues)
#numpy.save("data\\targetAnglesBackLeg.npy",targetAngles_BackLeg)
#numpy.save("data\\targetAnglesFrontLeg.npy",targetAngles_FrontLeg)
#exit()


    



'''

