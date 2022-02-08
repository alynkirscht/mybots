#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim

#Variables
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

#Tell pyrosim where info about world (box) should be stored
pyrosim.Start_SDF("boxes.sdf")

#Store a box with specific position and size
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[width,length,height])

#Store a box with specific position and size
pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[width,length,height])

#Close sdf file
pyrosim.End()

