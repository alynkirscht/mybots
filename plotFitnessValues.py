import numpy
import matplotlib.pyplot
import constants as c

# A is without any hidden neurons
# B is with 5 hidden neurons

import numpy
import matplotlib.pyplot

def main():
    #matrix()
    #figure()
    #plot_mean()
    std_dev()
    #plot_all_means()
    #plot_trial(1)
    #plot_all_best()
    #plot_trial(4)

def plot_all_best():
    A_mins = [0] * c.numTrials
    B_mins = [0] * c.numTrials

    trials = []

    for i in range (0, c.numTrials):
        trials.append(i)

    for i in range(0,c.numTrials):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")

        i = int(i)

        A_mins [i-1] = A.min()
        B_mins [i-1] = B.min()

    matplotlib.pyplot.plot(trials, A_mins, color="blue", label = "No Hidden Neurons")
    matplotlib.pyplot.plot(trials, B_mins, color="yellow", label = "5 Hidden Neurons")
    matplotlib.pyplot.legend(loc="upper left")

    matplotlib.pyplot.title("Best Fitness")
    matplotlib.pyplot.xlabel("Trial")
    matplotlib.pyplot.ylabel("Fitness Value")



    matplotlib.pyplot.show()




    print(A_mins)
    print(B_mins)

    i = int(i)

def plot_all_means():
    for i in range(0,c.numTrials):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")
        A = numpy.mean(A, axis = 0)
        B = numpy.mean(B, axis = 0)

        if i == "1":
            matplotlib.pyplot.plot(A, color = "red", label = "Variant A")
            matplotlib.pyplot.plot(B, color = "blue", label = "Variant B")

        else:
            matplotlib.pyplot.plot(A, color = "red")
            matplotlib.pyplot.plot(B, color = "blue")
        print(i)


    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Plot All Means")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()
    i = int(i)


def plot_mean():

    A1 = numpy.load("matrixA1.npy")
    A2 = numpy.load("matrixA2.npy")
    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)


    A = numpy.mean(numpy.array([A1, A2], dtype=object), axis=0)


    B1 = numpy.load("matrixB1.npy")
    B2 = numpy.load("matrixB2.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)

    B = numpy.mean(numpy.array([B1, B2], dtype=object), axis=0)

    sA = numpy.std(A)
    sB = numpy.std(B)

    matplotlib.pyplot.plot(A, label = "Variant A")
  
    matplotlib.pyplot.plot(B, label = "Variant B")




    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Plot Mean")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


def std_dev():
    A1 = numpy.load("matrixA1.npy")
    A2 = numpy.load("matrixA2.npy")
    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)


    A = numpy.mean(numpy.array([A1, A2], dtype=object), axis=0)


    B1 = numpy.load("matrixB1.npy")
    B2 = numpy.load("matrixB2.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)

    B = numpy.mean(numpy.array([B1, B2], dtype=object), axis=0)

    sA = numpy.std(A)
    sB = numpy.std(B)

    matplotlib.pyplot.plot(A+sA, color = "navy", label = "Variant A +stdev")
    matplotlib.pyplot.plot(A, color = "blue", label = "Variant A")
    matplotlib.pyplot.plot(A-sA, color = "cornflowerblue", label = "Variant A -stdev")
 
    matplotlib.pyplot.plot(B+sB, color = "orangered", label = "Variant B +stdev")    
    matplotlib.pyplot.plot(B, color = "orange", label = "Variant B")
    matplotlib.pyplot.plot(B-sB, color = "gold", label = "Variant B -stdev")



    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Plot Standard Deviation")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()

def figure():
    # Load the fitness matrices from the .npy files
    fitnessMatrixA = numpy.load("matrixA1.npy")
    fitnessMatrixB = numpy.load("matrixB1.npy")

    # Plot each row of the "A" matrix as thin lines
    for i in range(fitnessMatrixA.shape[0]):
        matplotlib.pyplot.plot(fitnessMatrixA[i,:], linewidth=0.5, label="Variant A, Parent {}".format(i+1))

    # Plot each row of the "B" matrix as thick lines
    for i in range(fitnessMatrixB.shape[0]):
        matplotlib.pyplot.plot(fitnessMatrixB[i,:], linewidth=2, label="Variant B, Parent {}".format(i+1))

    # Add title and axis labels
    matplotlib.pyplot.title("Fitness Values Over Time")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness")

    # Add legend
    matplotlib.pyplot.legend()

    # Show the plot
    matplotlib.pyplot.show()

def matrix():
    # Create an empty fitness matrix
    fitnessMatrix = numpy.zeros((c.populationSize, c.numberOfGenerations))

    # Open the fitness file for reading
    with open("fitness.txt", "r") as f:
        # Loop over each generation
        for j in range(c.numberOfGenerations):
            # Loop over each parent in the generation
            for i in range(c.populationSize):
                try:
                    fitness = float(next(f).strip())
                except StopIteration:
                    # Handle case where there are no more lines in the file
                    break
                # Store the fitness value in the fitness matrix
                fitnessMatrix[i][j] = fitness
            # Increment the index of the file lines by population size to go to the next generation
            """ for k in range(c.populationSize):
                try:
                    next(f)
                except StopIteration:
                    break"""
    
    numpy.savetxt("matrix" + "B3" + ".csv", fitnessMatrix, delimiter =', ')
    numpy.save("matrix" + "B3" + ".npy", fitnessMatrix)

main()