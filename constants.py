import numpy
PI = numpy.pi
GRAVITY = -9.8
REPETITIONS = 1000
AMPLITUDE = PI/4
FREQUECY = 10
MAX_SIN = 2*PI
MIN_SIN = 0
OFFSET= 0
MAX_FORCE = 15
SLEEP_TIME = 1/999999999
TIMESTEP = 1/600
numberOfGenerations = 1 
populationSize = 1
motorJointRange = 0.5
numHiddenNeurons = 5
currentlyTesting = "ts_600_A"
massChange = 0
#restitutionChange = 0
#restitution = 0
#length_y = 0
#burn_in_denominator = numberOfGenerations/3

'''
# List of test cases
test_cases = ["burn_in_0_A", "burn_in_0_B", "burn_in_0_C", "burn_in_0_D", "burn_in_0_E"]

# Loop through each test case
for test_case in test_cases:
    # Set the currently testing variable
    currentlyTesting = test_case
    
    # Execute the search.py file
    subprocess.run(['python', 'search.py'])'''

