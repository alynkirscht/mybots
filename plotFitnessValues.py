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
    #mann_whitney_u()
    #convert_numpy()
    #scatterplot_all()
    #scatterplot_single()
    min_z()

def std_dev():
    add_remove = "burn_in"
    
    af0_data = numpy.empty((0,30), dtype=float)
    af_data = numpy.empty((0, 30), dtype=float)
    af1_data = numpy.empty((0, 30), dtype=float)
    #af01_data = numpy.empty((0, 30), dtype=float)
    #af001_data = numpy.empty((0, 30), dtype=float)
    #af0001_data = numpy.empty((0, 30), dtype=float)
    #afRandom_data = numpy.empty((0, 30), dtype=float)
    characters = ['A', 'B', 'C', 'D', 'E']

    for char in characters:
        # Load data
        af0 = numpy.load(f"burn_in2\matrix_{add_remove}_0_{char}.npy")
        af = numpy.load(f"burn_in2\matrix_{add_remove}_1_{char}.npy")
        af1 = numpy.load(f"burn_in2\matrix_{add_remove}_N_{char}.npy")
        #af01 = numpy.load(f"burn_in2\matrix_{add_remove}_15_{char}.npy")
        #af001 = numpy.load(f"burn_in2\matrix_{add_remove}_30_{char}.npy")
        #af0001 = numpy.load(f"burn_in2\matrix_{add_remove}_.0001_{char}.npy")
        #afRandom = numpy.load(f"burn_in2\matrix_{add_remove}_Random_{char}.npy")

        # Stack the loaded data for each variable vertically
        af0_data = numpy.vstack((af0_data, af0))
        af_data = numpy.vstack((af_data, af))
        af1_data = numpy.vstack((af1_data, af1))
        #af01_data = numpy.vstack((af01_data, af01))
        #af001_data = numpy.vstack((af001_data, af001))
        #af0001_data = numpy.vstack((af0001_data, af0001))
        #afRandom_data = numpy.vstack((afRandom_data, afRandom))
    
    af0_lower = numpy.zeros(c.numberOfGenerations)
    af_lower = numpy.zeros(c.numberOfGenerations)
    af1_lower = numpy.zeros(c.numberOfGenerations)
    #af01_lower = numpy.zeros(c.numberOfGenerations)
    #af001_lower = numpy.zeros(c.numberOfGenerations)
    #af0001_lower = numpy.zeros(c.numberOfGenerations)
    #afRandom_lower = numpy.zeros(c.numberOfGenerations)
    af0_upper = numpy.zeros(c.numberOfGenerations)
    af_upper = numpy.zeros(c.numberOfGenerations)
    af1_upper = numpy.zeros(c.numberOfGenerations)
    #af01_upper = numpy.zeros(c.numberOfGenerations)
    #af001_upper = numpy.zeros(c.numberOfGenerations)
    #af0001_upper = numpy.zeros(c.numberOfGenerations)
    #afRandom_upper = numpy.zeros(c.numberOfGenerations)

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

        #af01CIs = bootstrap.ci(data=af01_data[:,generation],statfunction=numpy.mean)
        #af01_lower[generation] = af01CIs[0]
        #af01_upper[generation] = af01CIs[1]

        #af001CIs = bootstrap.ci(data=af001_data[:,generation],statfunction=numpy.mean)
        #af001_lower[generation] = af001CIs[0]
        #af001_upper[generation] = af001CIs[1]

        #af0001CIs = bootstrap.ci(data=af0001_data[:,generation],statfunction=numpy.mean)
        #af0001_lower[generation] = af0001CIs[0]
        #af0001_upper[generation] = af0001CIs[1]

        #afRandomCIs = bootstrap.ci(data=afRandom_data[:,generation],statfunction=numpy.mean)
        #afRandom_lower[generation] = afRandomCIs[0]
        #afRandom_upper[generation] = afRandomCIs[1]

    # Calculate the overall means
    mean_af0 = numpy.mean(numpy.array(af0_data), axis=0)
    mean_af = numpy.mean(numpy.array(af_data), axis=0)
    mean_af1 = numpy.mean(numpy.array(af1_data), axis=0)
    #mean_af01 = numpy.mean(numpy.array(af01_data), axis=0)
    #mean_af001 = numpy.mean(numpy.array(af001_data), axis=0)
    #mean_af0001 = numpy.mean(numpy.array(af0001_data), axis=0)
    #mean_afRandom = numpy.mean(numpy.array(afRandom_data), axis=0)
    
    generations = numpy.arange(c.numberOfGenerations)

    # Plot the means
    matplotlib.pyplot.plot(mean_af0, label="No block added", color="red")
    matplotlib.pyplot.fill_between(generations, af0_lower, af0_upper, alpha=0.4, color="red")

    matplotlib.pyplot.plot(mean_af, label="1 whole block added", color="blue")
    matplotlib.pyplot.fill_between(generations, af_lower, af_upper, alpha=0.4, color="blue")

    matplotlib.pyplot.plot(mean_af1, label="1 Block added with burn-in", color="green")
    matplotlib.pyplot.fill_between(generations, af1_lower, af1_upper, alpha=0.4, color="green")

    #matplotlib.pyplot.plot(mean_af01, label="1 Block added with burn in of 15", color="lime")
    #matplotlib.pyplot.fill_between(generations, af01_lower, af01_upper, alpha=0.4, color="lime")

    #matplotlib.pyplot.plot(mean_af001, label="1 Block added with burn in of 30", color="green")
    #matplotlib.pyplot.fill_between(generations, af001_lower, af001_upper, alpha=0.4, color="green")

    #matplotlib.pyplot.plot(mean_af0001, label="0.0001", color="blue")
    #matplotlib.pyplot.fill_between(generations, af0001_lower, af0001_upper, alpha=0.4, color="blue")

    #matplotlib.pyplot.plot(mean_afRandom, label="Random", color="purple")
    #matplotlib.pyplot.fill_between(generations, afRandom_lower, afRandom_upper, alpha=0.4, color="purple")

    matplotlib.pyplot.legend(loc="lower left")
    matplotlib.pyplot.title("Fitness Curve for Adding Block with Burn In from Sensory to Hidden Neurons")
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
        af0 = numpy.load(f"burn_in2\matrix_{add_remove}_0_{char}.npy")
        af = numpy.load(f"burn_in2\matrix_{add_remove}_1_{char}.npy")
        af1 = numpy.load(f"burn_in2\matrix_{add_remove}_.1_{char}.npy")
        af01 = numpy.load(f"burn_in2\matrix_{add_remove}_.01_{char}.npy")
        af001 = numpy.load(f"burn_in2\matrix_{add_remove}_.001_{char}.npy")
        af0001 = numpy.load(f"burn_in2\matrix_{add_remove}_.0001_{char}.npy")
        afRandom = numpy.load(f"burn_in2\matrix_{add_remove}_Random_{char}.npy")

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

def convert_numpy():
## FOR SOME REASON i CAN'T REMOVE QUOTATION MARKS USING PYTHON, BEFORE RUNNING THIS FUNCTION USE REPLACE ON IDE (ctrl + H in VSCode)
# Loop over letters from 'a' to 'j'
    #for number in [480,540]:
    for timestep in ['240', '360', '480', '600']:
        for num in ['10', '8', '6', '4']:
            for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                # Construct the file name based on the changing letter
                csv_file = f"dataTimeSteps3\z__matrix_ts_{timestep}_{num}_{letter}.csv"
                    
                # Convert csv to numpy array
                data_array = numpy.loadtxt(csv_file, delimiter=',')            
                np_file = f"dataTimeSteps3\z__matrix_ts{timestep}_{num}_{letter}.npy"
                numpy.save(np_file, data_array)

def scatterplot_all():
    # List of changing letters
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # List to store the data for each letter
    data_4 = []
    data_6 = []
    data_8 = []
    data_10 = []

    for letter in letters:
        # Load data for each letter and append it to the list
        data_4.append(numpy.load(f"z_matrix_error_4_{letter}.npy"))
        data_6.append(numpy.load(f"z_matrix_error_6_{letter}.npy"))
        data_8.append(numpy.load(f"z_matrix_error_8_{letter}.npy"))
        data_10.append(numpy.load(f"z_matrix_error_10_{letter}.npy"))

    # Convert the list to a NumPy array
    data_4_array = numpy.array(data_4)
    data_6_array = numpy.array(data_6)
    data_8_array = numpy.array(data_8)
    data_10_array = numpy.array(data_10)

    # Calculate the mean along the first axis (axis=0)
    mean_d4 = numpy.mean(data_4_array, axis=0)
    mean_d6 = numpy.mean(data_6_array, axis=0)
    mean_d8 = numpy.mean(data_8_array, axis=0)
    mean_d10 = numpy.mean(data_10_array, axis=0)


    # Plot scatterplot
    matplotlib.pyplot.scatter(range(len(mean_d4[:, -1])), mean_d4[:, -1], s=0.5, label='Length of 4 blocks')
    matplotlib.pyplot.scatter(range(len(mean_d6[:, -1])), mean_d6[:, -1], s=0.5, label='Length of 6 blocks')
    matplotlib.pyplot.scatter(range(len(mean_d8[:, -1])), mean_d8[:, -1], s=0.5, label='Length of 8 blocks')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, -1])), mean_d10[:, -1], s=0.5, label='Length of 10 blocks')
    matplotlib.pyplot.axhline(y=0.5, color='r', linestyle='--', linewidth=0.5)
    
    # Set labels and title
    matplotlib.pyplot.xlabel('Timesteps')
    matplotlib.pyplot.ylabel('Average Z-coordinate for last block')
    matplotlib.pyplot.title('Average Z-coordinate for Last Block Over Timesteps')

    # Add legend
    matplotlib.pyplot.legend(markerscale=10)

    # Show the plot
    matplotlib.pyplot.show()

def scatterplot_single():
    # List of changing letters
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # List to store the data for each letter
    data_4 = []
    data_6 = []
    data_8 = []
    data_10 = []

    for letter in letters:
        # Load data for each letter and append it to the list
        data_4.append(numpy.load(f"z_matrix_error_4_{letter}.npy"))
        data_6.append(numpy.load(f"z_matrix_error_6_{letter}.npy"))
        data_8.append(numpy.load(f"z_matrix_error_8_{letter}.npy"))
        data_10.append(numpy.load(f"z_matrix_error_10_{letter}.npy"))

    # Convert the list to a NumPy array
    data_4_array = numpy.array(data_4)
    data_6_array = numpy.array(data_6)
    data_8_array = numpy.array(data_8)
    data_10_array = numpy.array(data_10)

    # Calculate the mean along the first axis (axis=0)
    mean_d4 = numpy.mean(data_4_array, axis=0)
    mean_d6 = numpy.mean(data_6_array, axis=0)
    mean_d8 = numpy.mean(data_8_array, axis=0)
    mean_d10 = numpy.mean(data_10_array, axis=0)


    # Plot scatterplot
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 0])), mean_d10[:, 0], s=0.5, label='Block 1')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 1])), mean_d10[:, 1], s=0.5, label='Block 2')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 2])), mean_d10[:, 2], s=0.5, label='Block 3')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 3])), mean_d10[:, 3], s=0.5, label='Block 4')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 4])), mean_d10[:, 4], s=0.5, label='Block 5')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 5])), mean_d10[:, 5], s=0.5, label='Block 6')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 6])), mean_d10[:, 6], s=0.5, label='Block 7')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 7])), mean_d10[:, 7], s=0.5, label='Block 8')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 8])), mean_d10[:, 8], s=0.5, label='Block 9')
    matplotlib.pyplot.scatter(range(len(mean_d10[:, 9])), mean_d10[:, 9], s=0.5, label='Block 10')
    matplotlib.pyplot.axhline(y=0.5, color='r', linestyle='--', linewidth=0.5)
    
    # Set labels and title
    matplotlib.pyplot.xlabel('Timesteps')
    matplotlib.pyplot.ylabel('Average Z-coordinate for all blocks')
    matplotlib.pyplot.title('Average Z-coordinate for All Blocks (Length 10)')

    # Add legend
    matplotlib.pyplot.legend(markerscale=10)

    # Show the plot
    matplotlib.pyplot.show()

def min_z():
    # List of changing sizes
    sizes = ['10', '8', '6', '4']

    # Define a color map for sizes
    color_map = {'10': 'blue', '8': 'green', '6': 'red', '4': 'orange'}

    # List to store the minimum z-values for each size and timestep
    min_z_values = {size: {} for size in sizes}

    # Load data for each size and timestep and calculate the minimum z-value
    for size in sizes:
        for timestep in ['240', '360', '480', '600']:
            # List to store the minimum z-values for the current timestep
            min_z_values[size][timestep] = []

            # Load data for each letter and calculate the minimum z-value
            for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                data_array = numpy.load(f"dataTimeSteps3\z__matrix_ts{timestep}_{size}_{letter}.npy")
                min_z_values[size][timestep].append(numpy.min(data_array))

            # Calculate the overall minimum z-value for the current timestep and size
            min_z_values[size][timestep] = min(min_z_values[size][timestep])

    # Plot min z-coordinate for each timestep and size
    for size in sizes:
        min_z_values_list = [min_z_values[size][timestep] - 0.5 for timestep in ['240', '360', '480', '600']]
        matplotlib.pyplot.scatter([int(timestep) for timestep in ['240', '360', '480', '600']], min_z_values_list, label=f"Size {size}", color=color_map[size])

    # Set labels and title
    matplotlib.pyplot.xlabel('Timestep size (Hz)')
    matplotlib.pyplot.ylabel('Min Z-coordinate - 0.5')
    matplotlib.pyplot.title('Min Z-coordinate - 0.5 for Different Timesteps and Sizes')

    # Show the plot
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()
    

main()