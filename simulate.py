#Alyn Kirsch Tornell
#This program simulates the world robots will live in
import pybullet as p
import time
import pybullet_data

#Create objects that handles physics and draws results to GUI
physicsClient = p.connect(p.GUI)

#Create normal force generated when hitting floor
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Add force of gravity
p.setGravity(0,0,-9.8)

#Add floor
planeId = p.loadURDF("plane.urdf")
p.changeDynamics(planeId, -1, restitution=0.5)

#Add robots
#box1 = p.loadURDF("box1.urdf")
box2 = p.loadURDF("box2.urdf")
box3 = p.loadSoftBody("box3.urdf")
#p.changeDynamics(box1, -1, restitution = 1.0)  # Adjust friction and restitution as needed
p.changeDynamics(box2, -1, restitution=1.0)  # Adjust friction and restitution as needed


#The for loop is used to slow things down
for i in range(1000):
    #Steps physics inside the world
    p.stepSimulation()
    #Slows things down by 1/60 second of each iteration of the loop
    time.sleep(1/60)
    #print (i)
p.disconnect()