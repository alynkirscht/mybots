import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT
import time
import csv
import robot

class SIMULATION:
    def __init__(self, directOrGUI, solutionID, restitution, num_links):
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        elif (directOrGUI == "GUI"):
            self.physicsClient = p.connect(p.GUI)
            
        #Create normal force generated when hitting floor
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #Add force of gravity
        p.setGravity(0,0,c.GRAVITY)
        
        self.solutionID = solutionID
        self.robot = ROBOT(self.solutionID, restitution, num_links)
        self.world = WORLD()

        self.directOrGUI = directOrGUI

        self.snake_robot_ids = list(range(c.populationSize))

        # Initialize a matrix to store z-positions for each snake
        self.z_positions_matrix = [[] for _ in range(c.populationSize)]
        
    def __del__(self):
        p.disconnect()

    
    def Run(self):
        #The for loop is used to slow things down
        for i in range(c.REPETITIONS):
            
            #Steps physics inside the world
            p.stepSimulation()

            #Enable sensing in robot
            self.robot.Sense(i)

            #Enable thinking in the robot
            self.robot.Think()

            #Enable acting in robot
            self.robot.Act(i)

            if (self.directOrGUI == "GUI"):
                time.sleep(c.SLEEP_TIME) 
            """
            for snake_idx, robot_id in enumerate(self.snake_robot_ids):
                # Get and store z-positions of links for each snake
                link_z_positions = []
                basePositionAndOrientation = p.getBasePositionAndOrientation(robot_id)
                basePosition = basePositionAndOrientation[0]
                root_z = basePosition[2]
                link_z_positions.append(root_z)
                for link_idx in range(p.getNumJoints(robot_id)):
                    link_state = p.getLinkState(robot_id, link_idx, computeLinkVelocity=1, computeForwardKinematics=1)
                    link_z_pos = link_state[0][2]  # Extracting the z-position
                    link_z_positions.append(link_z_pos)
                
                # Append z-positions to the corresponding row in the matrix
                self.z_positions_matrix[snake_idx].append(link_z_positions)

        # Store z-positions matrix in a CSV file
        csv_file = "z__matrix_" +  c.currentlyTesting + ".csv"
        with open(csv_file, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write z-positions for each snake
            for row in zip(*self.z_positions_matrix):
                csv_writer.writerow(row) # Unpack the row list and write it to the CSV file
        """    
            
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)
        
            

