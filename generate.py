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

#Iterate 10 times to create 10 boxes vertically
for i in range(10):
    
    #Iterate 5 times to create 5 rows
    for j in range(5):

        #Iterate 5 times to create 5 columns
        for k in range(5):

            #Store a box with specific position and size
            pyrosim.Send_Cube(name="Box", pos=[x + j,y + k,z + i] ,
                              size=[width * (.9)**i,
                                    length * (.9)**i,
                                    height * (.9)**i])

#Close sdf file
pyrosim.End()

