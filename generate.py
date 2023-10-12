#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim
#Create_World creates the simulated world, with a box in it
def Create_World():
    
    #Tell pyrosim where info about world (world) should be stored
    pyrosim.Start_SDF("plane.sdf")
    #pyrosim.Start_SDF("box.sdf")
    #pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])


    #Close sdf file
    pyrosim.End()

#Create_Robot creates a robot
def Create_Robot():
    '''
    #Tell pyrosim where info about body of the robot should be stored
    pyrosim.Start_URDF("box1.urdf")
    #Store Link0 with specific position and size
    pyrosim.Send_Cube(name="s0", pos=[0,0,.5], size=[1, 1, 1], restitution=1)

    pyrosim.End()
    '''

    """#Joint to connect Link0 and Link1 and Torso
    pyrosim.Send_Joint( name = "s0_s1", parent = "s0", child = "s1",
                        type = "revolute", position = [0,0.5,0.5])"""
    
    pyrosim.Start_URDF("box2.urdf")
    #Store Link1 with specific position and size
    pyrosim.Send_Cube(name="s1", pos=[0,0,3], size=[1, 1, 1],restitution=1)
    
    pyrosim.End()

    
    
Create_World()
Create_Robot()




    