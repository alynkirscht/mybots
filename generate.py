#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim

#Variables
length = 1
width = 2
height = 3

#Tell pyrosim where info about world (box) should be stored
pyrosim.Start_SDF("box.sdf")

#Store a box with specific position and size
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[width,length,height])

#Close sdf file
pyrosim.End()

