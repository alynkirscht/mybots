import numpy
import matplotlib.pyplot
import constants as c
from scipy.stats import mannwhitneyu


# A is without any hidden neurons
# B is with 5 hidden neurons

def main():
    #matrix()
    #figure()
    plot_mean()
    #std_dev()
    #plot_all_means()
    #plot_trial(1)
    #plot_all_best()
    #plot_trial(4)
    #mann_whitney_u()

def plot_all_best():
    A_mins = [0] * c.numTrials
    B_mins = [0] * c.numTrials

    trials = []

    for i in range (0, c.numTrials):
        trials.append(i)

    for i in range(0,c.numTrials):
        i = str(i)
        A = numpy.load("data/matrixA" + i + ".npy")
        B = numpy.load("data/matrixB" + i + ".npy")

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
    for i in range(1,5):
        i = str(i)
        A = numpy.load("data/matrixA" + i + ".npy")
        B = numpy.load("data/matrixB" + i + ".npy")
        A = numpy.mean(A, axis = 0)
        B = numpy.mean(B, axis = 0)

        if i == "1":
            matplotlib.pyplot.plot(A, color = "blue", label = "Variant A")
            matplotlib.pyplot.plot(B, color = "red", label = "Variant B")

        else:
            matplotlib.pyplot.plot(A, color = "blue")
            matplotlib.pyplot.plot(B, color = "red")
        


    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Plot All Means")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()
    i = int(i)


def plot_mean():

    A1 = numpy.load("data/matrixA1.npy")
    A2 = numpy.load("data/matrixA2.npy")
    A3 = numpy.load("data/matrixA3.npy")
    A4 = numpy.load("data/matrixA4.npy")
    A5 = numpy.load("data/matrixA5.npy")


    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)
    A3 = numpy.mean(A3, axis = 0)
    A4 = numpy.mean(A4, axis = 0)
    A5 = numpy.mean(A5, axis = 0)

    A = numpy.mean(numpy.array([A1, A2, A3, A4, A5], dtype=object), axis=0)


    B1 = numpy.load("data/matrixB1.npy")
    B2 = numpy.load("data/matrixB2.npy")
    B3 = numpy.load("data/matrixB3.npy")
    B4 = numpy.load("data/matrixB4.npy")
    B5 = numpy.load("data/matrixB5.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)
    B3 = numpy.mean(B3, axis = 0)
    B4 = numpy.mean(B4, axis = 0)
    B5 = numpy.mean(B5, axis = 0)

    B = numpy.mean(numpy.array([B1, B2, B3, B4, B5], dtype=object), axis=0)

    matplotlib.pyplot.plot(A, label = "Variant A", color="blue")
  
    matplotlib.pyplot.plot(B, label = "Variant B", color="red")

    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Fitness Curve")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


def std_dev():
    A1 = numpy.load("data/matrixA1.npy")
    A2 = numpy.load("data/matrixA2.npy")
    A3 = numpy.load("data/matrixA3.npy")
    A4 = numpy.load("data/matrixA4.npy")
    A5 = numpy.load("data/matrixA5.npy")


    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)
    A3 = numpy.mean(A3, axis = 0)
    A4 = numpy.mean(A4, axis = 0)
    A5 = numpy.mean(A5, axis = 0)

    A = numpy.mean(numpy.array([A1, A2, A3, A4, A5], dtype=object), axis=0)


    B1 = numpy.load("data/matrixB1.npy")
    B2 = numpy.load("data/matrixB2.npy")
    B3 = numpy.load("data/matrixB3.npy")
    B4 = numpy.load("data/matrixB4.npy")
    B5 = numpy.load("data/matrixB5.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)
    B3 = numpy.mean(B3, axis = 0)
    B4 = numpy.mean(B4, axis = 0)
    B5 = numpy.mean(B5, axis = 0)

    B = numpy.mean(numpy.array([B1, B2, B3, B4, B5], dtype=object), axis=0)


    sA = numpy.std(A)
    sB = numpy.std(B)

    matplotlib.pyplot.plot(A+sA, color = "cornflowerblue", label = "Variant A +/- stdev")
    matplotlib.pyplot.plot(A, color = "blue", label = "Variant A")
    matplotlib.pyplot.plot(A-sA, color = "cornflowerblue")
 
    matplotlib.pyplot.plot(B+sB, color = "orange", label = "Variant B +/1 stdev")    
    matplotlib.pyplot.plot(B, color = "red", label = "Variant B")
    matplotlib.pyplot.plot(B-sB, color = "orange")



    matplotlib.pyplot.legend(loc="upper right")
    matplotlib.pyplot.title("Fitness Curves with Std Deviations")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()

def figure():
    # Load the fitness matrices from the .npy files
    fitnessMatrixA1 = numpy.load("data/matrixA1.npy")
    fitnessMatrixB1 = numpy.load("data/matrixB1.npy")
    fitnessMatrixA2 = numpy.load("data/matrixA2.npy")
    fitnessMatrixB2 = numpy.load("data/matrixB2.npy")
    fitnessMatrixA3 = numpy.load("data/matrixA3.npy")
    fitnessMatrixB3 = numpy.load("data/matrixB3.npy")
    fitnessMatrixA4 = numpy.load("data/matrixA4.npy")
    fitnessMatrixB4 = numpy.load("data/matrixB4.npy")
    fitnessMatrixA5 = numpy.load("data/matrixA5.npy")
    fitnessMatrixB5 = numpy.load("data/matrixB5.npy")
    '''
    # Plot each row of the "A" matrix as thin lines
    for i in range(fitnessMatrixA1.shape[0]):
        matplotlib.pyplot.plot(fitnessMatrixA1[i,:], color="blue", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixA2[i,:], color="blue", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixA3[i,:], color="blue", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixA4[i,:], color="blue", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixA5[i,:], color="blue", linewidth=0.5)
    '''
    # Plot each row of the "B" matrix as thick lines
    for i in range(fitnessMatrixB1.shape[0]):
        matplotlib.pyplot.plot(fitnessMatrixB1[i,:], color="red", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixB2[i,:], color="red", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixB3[i,:], color="red", linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixB4[i,:], color="red",linewidth=0.5)
        matplotlib.pyplot.plot(fitnessMatrixB5[i,:], color="red",linewidth=0.5)

    # Add title and axis labels
    matplotlib.pyplot.title("Fitness Curves with Hidden Neurons")
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
    
    numpy.savetxt("data/matrix" + "B3" + ".csv", fitnessMatrix, delimiter =', ')
    numpy.save("data/matrix" + "B3" + ".npy", fitnessMatrix)
    
def mann_whitney_u():
    a_first = []
    a_last = []
    b_first = []
    b_last = []

    fitnessMatrixA1 = numpy.load("data/matrixA1.npy")
    fitnessMatrixB1 = numpy.load("data/matrixB1.npy")
    fitnessMatrixA2 = numpy.load("data/matrixA2.npy")
    fitnessMatrixB2 = numpy.load("data/matrixB2.npy")
    fitnessMatrixA3 = numpy.load("data/matrixA3.npy")
    fitnessMatrixB3 = numpy.load("data/matrixB3.npy")
    fitnessMatrixA4 = numpy.load("data/matrixA4.npy")
    fitnessMatrixB4 = numpy.load("data/matrixB4.npy")
    fitnessMatrixA5 = numpy.load("data/matrixA5.npy")
    fitnessMatrixB5 = numpy.load("data/matrixB5.npy")

    for matrix in [fitnessMatrixA1, fitnessMatrixA2, fitnessMatrixA3, fitnessMatrixA4, fitnessMatrixA5]:
        a_first += list(matrix[:, 0])
        a_last += list(matrix[:, -1])

    for matrix in [fitnessMatrixB1, fitnessMatrixB2, fitnessMatrixB3, fitnessMatrixB4, fitnessMatrixB5]:
        b_first += list(matrix[:, 0])
        b_last += list(matrix[:, -1])


    U1, p = mannwhitneyu(a_first, a_last)
    print("Evolution in variant A: " + str(U1) + " p = " + str(p))
    U1, p = mannwhitneyu(b_first, b_last)
    print("Evolution in variant B: " + str(U1) + " p = " + str(p))

    U1, p = mannwhitneyu(a_first, b_first)
    print("Fair test? " + str(U1) + " p = " + str(p))

    U1, p = mannwhitneyu(a_last, b_last)
    print("Significant different? " + str(U1) + " p = " + str(p))




main()