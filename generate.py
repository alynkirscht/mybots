#Alyn Kirsch Tornell
#This program generates one link

import pyrosim.pyrosim as pyrosim
import random
#Create_World creates the simulated world, with a box in it
def Create_World():
    
    #Tell pyrosim where info about world (world) should be stored
    pyrosim.Start_SDF("world.sdf")

    #Store a box with specific position and size
    pyrosim.Send_Cube(name="Box", pos=[-2,2,.5], size=[1, 1, 1])

    #Close sdf file
    pyrosim.End()

def Generate_Body():

    #Tell pyrosim where info about body of the robot should be stored
    pyrosim.Start_URDF("body.urdf")
    
    #Torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1, 1, 1])
    
    #Joint to connect Torso and Backleg
    pyrosim.Send_Joint( name = "Torso_BackLeg", parent = "Torso", child = "BackLeg",
                        type = "revolute", position = [1,0,1])
    #BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5], size=[1, 1, 1])

    #Joint to connect Torso and FrontLeg
    pyrosim.Send_Joint( name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg",
                        type = "revolute", position = [2,0,1])
    #FrontLeg
    pyrosim.Send_Cube( name="FrontLeg", pos=[.5,0,-.5], size=[1,1,1])

    pyrosim.End()

def Generate_Brain():

    #Tell pyrosim where info about brain of the robot should be stored
    pyrosim.Start_NeuralNetwork("brain.nndf")

    #Send sensor neurons
    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

    '''pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 2.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 2.0 )'''

    for i in range(2):
        for j in range(3,5):
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j ,
                                  weight = random.uniform(-1,1) )
            
    
    pyrosim.End()
    
Create_World()
Generate_Body()
Generate_Brain()




    
