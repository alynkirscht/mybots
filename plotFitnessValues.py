import numpy
import matplotlib.pyplot
import constants as c
import scipy.stats as stats
import scikits.bootstrap as bootstrap
import csv


# A is without any hidden neurons
# B is with 5 hidden neurons

def main():
    #std_dev()
    mann_whitney_u()

def std_dev():
    add_remove = "8Remove"
    
    af0_data = numpy.empty((0,30), dtype=float)
    af_data = numpy.empty((0, 30), dtype=float)
    af1_data = numpy.empty((0, 30), dtype=float)
    af01_data = numpy.empty((0, 30), dtype=float)
    af001_data = numpy.empty((0, 30), dtype=float)
    af0001_data = numpy.empty((0, 30), dtype=float)
    afRandom_data = numpy.empty((0, 30), dtype=float)
    characters = ['A', 'B', 'C', 'D', 'E']

    for char in characters:
        # Load data
        af0 = numpy.load(f"dataMass\matrix_{add_remove}_0_{char}.npy")
        af = numpy.load(f"dataMass\matrix_{add_remove}_1_{char}.npy")
        af1 = numpy.load(f"dataMass\matrix_{add_remove}_.1_{char}.npy")
        af01 = numpy.load(f"dataMass\matrix_{add_remove}_.01_{char}.npy")
        af001 = numpy.load(f"dataMass\matrix_{add_remove}_.001_{char}.npy")
        af0001 = numpy.load(f"dataMass\matrix_{add_remove}_.0001_{char}.npy")
        afRandom = numpy.load(f"dataMass\matrix_{add_remove}_Random_{char}.npy")

        # Stack the loaded data for each variable vertically
        af0_data = numpy.vstack((af0_data, af0))
        af_data = numpy.vstack((af_data, af))
        af1_data = numpy.vstack((af1_data, af1))
        af01_data = numpy.vstack((af01_data, af01))
        af001_data = numpy.vstack((af001_data, af001))
        af0001_data = numpy.vstack((af0001_data, af0001))
        afRandom_data = numpy.vstack((afRandom_data, afRandom))
    
    af0_lower = numpy.zeros(c.numberOfGenerations)
    af_lower = numpy.zeros(c.numberOfGenerations)
    af1_lower = numpy.zeros(c.numberOfGenerations)
    af01_lower = numpy.zeros(c.numberOfGenerations)
    af001_lower = numpy.zeros(c.numberOfGenerations)
    af0001_lower = numpy.zeros(c.numberOfGenerations)
    afRandom_lower = numpy.zeros(c.numberOfGenerations)
    af0_upper = numpy.zeros(c.numberOfGenerations)
    af_upper = numpy.zeros(c.numberOfGenerations)
    af1_upper = numpy.zeros(c.numberOfGenerations)
    af01_upper = numpy.zeros(c.numberOfGenerations)
    af001_upper = numpy.zeros(c.numberOfGenerations)
    af0001_upper = numpy.zeros(c.numberOfGenerations)
    afRandom_upper = numpy.zeros(c.numberOfGenerations)

    for generation in range(c.numberOfGenerations):

        af0CIs = bootstrap.ci(data=af0_data[:,generation],statfunction=numpy.mean)
        af0_lower[generation] = af0CIs[0]
        af0_upper[generation] = af0CIs[1]

        afCIs = bootstrap.ci(data=af_data[:,generation],statfunction=numpy.mean)
        af_lower[generation] = afCIs[0]
        af_upper[generation] = afCIs[1]

        af1CIs = bootstrap.ci(data=af1_data[:,generation],statfunction=numpy.mean)
        af1_lower[generation] = af1CIs[0]
        af1_upper[generation] = af1CIs[1]

        af01CIs = bootstrap.ci(data=af01_data[:,generation],statfunction=numpy.mean)
        af01_lower[generation] = af01CIs[0]
        af01_upper[generation] = af01CIs[1]

        af001CIs = bootstrap.ci(data=af001_data[:,generation],statfunction=numpy.mean)
        af001_lower[generation] = af001CIs[0]
        af001_upper[generation] = af001CIs[1]

        af0001CIs = bootstrap.ci(data=af0001_data[:,generation],statfunction=numpy.mean)
        af0001_lower[generation] = af0001CIs[0]
        af0001_upper[generation] = af0001CIs[1]

        afRandomCIs = bootstrap.ci(data=afRandom_data[:,generation],statfunction=numpy.mean)
        afRandom_lower[generation] = afRandomCIs[0]
        afRandom_upper[generation] = afRandomCIs[1]

    # Calculate the overall means
    mean_af0 = numpy.mean(numpy.array(af0_data), axis=0)
    mean_af = numpy.mean(numpy.array(af_data), axis=0)
    mean_af1 = numpy.mean(numpy.array(af1_data), axis=0)
    mean_af01 = numpy.mean(numpy.array(af01_data), axis=0)
    mean_af001 = numpy.mean(numpy.array(af001_data), axis=0)
    mean_af0001 = numpy.mean(numpy.array(af0001_data), axis=0)
    mean_afRandom = numpy.mean(numpy.array(afRandom_data), axis=0)
    
    generations = numpy.arange(c.numberOfGenerations)

    # Plot the means
    matplotlib.pyplot.plot(mean_af0, label="0", color="red")
    matplotlib.pyplot.fill_between(generations, af0_lower, af0_upper, alpha=0.4, color="red")

    matplotlib.pyplot.plot(mean_af, label="1", color="orange")
    matplotlib.pyplot.fill_between(generations, af_lower, af_upper, alpha=0.4, color="orange")

    matplotlib.pyplot.plot(mean_af1, label="0.1", color="yellow")
    matplotlib.pyplot.fill_between(generations, af1_lower, af1_upper, alpha=0.4, color="yellow")

    matplotlib.pyplot.plot(mean_af01, label="0.01", color="lime")
    matplotlib.pyplot.fill_between(generations, af01_lower, af01_upper, alpha=0.4, color="lime")

    matplotlib.pyplot.plot(mean_af001, label="0.001", color="green")
    matplotlib.pyplot.fill_between(generations, af001_lower, af001_upper, alpha=0.4, color="green")

    matplotlib.pyplot.plot(mean_af0001, label="0.0001", color="blue")
    matplotlib.pyplot.fill_between(generations, af0001_lower, af0001_upper, alpha=0.4, color="blue")

    matplotlib.pyplot.plot(mean_afRandom, label="Random", color="purple")
    matplotlib.pyplot.fill_between(generations, afRandom_lower, afRandom_upper, alpha=0.4, color="purple")

    matplotlib.pyplot.legend(loc="lower left")
    matplotlib.pyplot.title("Fitness Curve for Removing Mass of Block (Size of snake: 8 links)")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()

def mann_whitney_u():
    add_remove = "8Remove"

    af0_first = []
    af0_last = []

    af_first = []
    af_last = []

    af1_first = []
    af1_last = []

    af01_first = []
    af01_last = []

    af001_first = []
    af001_last = []

    af0001_first = []
    af0001_last = []

    afRandom_first = []
    afRandom_last = []        

    characters = ['A', 'B', 'C', 'D', 'E']

    for char in characters:
        # Load data
        af0 = numpy.load(f"dataMass\matrix_{add_remove}_0_{char}.npy")
        af = numpy.load(f"dataMass\matrix_{add_remove}_1_{char}.npy")
        af1 = numpy.load(f"dataMass\matrix_{add_remove}_.1_{char}.npy")
        af01 = numpy.load(f"dataMass\matrix_{add_remove}_.01_{char}.npy")
        af001 = numpy.load(f"dataMass\matrix_{add_remove}_.001_{char}.npy")
        af0001 = numpy.load(f"dataMass\matrix_{add_remove}_.0001_{char}.npy")
        afRandom = numpy.load(f"dataMass\matrix_{add_remove}_Random_{char}.npy")

        af0_first += list(af0[:, 0])
        af0_last += list(af0[:, -1])

        af_first += list(af[:, 0])
        af_last += list(af[:, -1])

        af1_first += list(af1[:, 0])
        af1_last += list(af1[:, -1])

        af01_first += list(af01[:, 0])
        af01_last += list(af01[:, -1])

        af001_first += list(af001[:, 0])
        af001_last += list(af001[:, -1])

        af0001_first += list(af0001[:, 0])
        af0001_last += list(af0001[:, -1])

        afRandom_first += list(afRandom[:, 0])
        afRandom_last += list(afRandom[:, -1])

    comparisons_first = [af0_first, af_first, af1_first, af01_first, af001_first, af0001_first, afRandom_first]
    comparisons_last = [af0_last, af_last, af1_last, af01_last, af001_last, af0001_last, afRandom_last]
    matrix_first = []
    matrix_last = []
    num_comparisons = 11 #len(comparisons_first) * (len(comparisons_first) - 1)  # 15 unique comparisons
    bonferroni_alpha = .05 / num_comparisons

    matrix_first = []
    matrix_last = []
    num_comparisons = 11 #len(comparisons_first) * (len(comparisons_first) - 1)  # 15 unique comparisons
    bonferroni_alpha = .05 / num_comparisons
    print("BONFERRONI ALPHA", bonferroni_alpha)

    # Compare af to all
    rowf1 = [None]
    rowl1 = [None]

    # 1 v all
    count = 0
    print("FIRST 1")
    for data in comparisons_first[2:]:
        U, p = stats.mannwhitneyu(af_first, data)
        print(p * num_comparisons)
        rowf1.append(p * num_comparisons)
        count += 1

    # 1 v all
    count = 0
    print("LAST 1")
    for data in comparisons_last[2:]:
        U, p = stats.mannwhitneyu(af_last, data)
        print(p * num_comparisons)
        rowl1.append(p * num_comparisons)
        count += 1
    
    # Compare af0 to all
    rowf0 = [None]
    rowl0 = [None]

    # 0 v all
    count = 0
    print("FIRST 0")
    for data in comparisons_first[1:]:
        U, p = stats.mannwhitneyu(af0_first, data)
        print(p * num_comparisons)
        rowf0.append(p * num_comparisons)
        count += 1

    # 1 v all
    count = 0
    print("LAST 0")
    for data in comparisons_last[1:]:
        U, p = stats.mannwhitneyu(af0_last, data)
        print(p * num_comparisons)
        rowl0.append(p * num_comparisons)
        count += 1

    file = f"MannWhitney_firstGen_{add_remove}.csv"
    with open(file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        print(matrix_first)
        for row in matrix_first:
            csv_writer.writerow(row)

    file = f"MannWhitney_lastGen_{add_remove}.csv"
    with open(file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in matrix_last:
            csv_writer.writerow(row)

main()