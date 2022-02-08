#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim
#Create_World creates the simulated world, with a box in it
def Create_World():
    #Variables
    length = 1
    width = 1
    height = 1
    x = -2
    y = 2
    z = .5
    
    #Tell pyrosim where info about world (world) should be stored
    pyrosim.Start_SDF("world.sdf")

    #Store a box with specific position and size
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[width, length, height])

    #Close sdf file
    pyrosim.End()

#Create_Robot creates a robot
def Create_Robot():
    #Variables
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = .5

    #Tell pyrosim where info about body of the robot should be stored
    pyrosim.Start_URDF("body.urdf")
    #Store a torso with specific position and size
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[width, length, height])
    pyrosim.End()
    
Create_World()
Create_Robot()




    
