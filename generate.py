#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim
#Create_World creates the simulated world, with a box in it
def Create_World():
    
    #Tell pyrosim where info about world (world) should be stored
    pyrosim.Start_SDF("world.sdf")

    #Store a box with specific position and size
    #pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[1, 1, 1])

    #Close sdf file
    pyrosim.End()

#Create_Robot creates a robot
def Create_Robot():

    #Tell pyrosim where info about body of the robot should be stored
    pyrosim.Start_URDF("body.urdf")
    #Store Link0 with specific position and size
    pyrosim.Send_Cube(name="Link0", pos=[0,0,.5], size=[1, 1, 1])

    #Joint to connect Link0 and Link1 and Torso
    pyrosim.Send_Joint( name = "Link0_Link1", parent = "Link0", child = "Link1",
                        type = "revolute", position = [0,0,1])
    
    #Store Link1 with specific position and size
    pyrosim.Send_Cube(name="Link1", pos=[0,0,.5], size=[1, 1, 1])
    

    #Joint between Link1 and Link2
    pyrosim.Send_Joint( name = "Link1_Link2", parent = "Link1", child = "Link2",
                        type = "revolute", position = [0,0,1])
    #Link2
    pyrosim.Send_Cube( name="Link2", pos=[0,0,.5], size=[1,1,1])

    #Joint between Link2 and Link3
    pyrosim.Send_Joint( name = "Link2_Link1", parent = "Link2", child = "Link3",
                        type = "revolute", position = [0,.5,.5])

    #Link3
    pyrosim.Send_Cube( name="Link3", pos=[0,.5,0], size=[1,1,1])

    #Joint between Link3 and Link4
    pyrosim.Send_Joint( name = "Link3_Link4", parent = "Link3", child = "Link4",
                        type = "revolute", position = [0,1,0])

    #Link4
    pyrosim.Send_Cube( name="Link4", pos=[0,.5,0], size=[1,1,1])

    #Joint between Link4 and Link5
    pyrosim.Send_Joint( name = "Link4_Link5", parent = "Link4", child = "Link5",
                        type = "revolute", position = [0,0.5,-0.5])

    #Link5
    pyrosim.Send_Cube( name="Link5", pos=[0,0,-.5], size=[1,1,1])

    #Joint between Link5 and Link6
    pyrosim.Send_Joint( name = "Link5_Link6", parent = "Link5", child = "Link6",
                        type = "revolute", position = [0,0,-1])

    #Link6
    pyrosim.Send_Cube( name="Link6", pos=[0,0,-.5], size=[1,1,1])
    
    pyrosim.End()

    
    
Create_World()
Create_Robot()




    
