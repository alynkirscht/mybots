import csv
import constants as c

def merge_rows():
    # Read the input CSV file
    with open('data\\4seg_final.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)

    merged_rows = []
    for i in range(0, len(rows) - 1,2):
        merged_row = rows[i] + rows[i+1]
        merged_rows.append(merged_row)

    # Write the merged data to a new CSV file
    with open('data\\4seg_parents.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(merged_rows)

def parents():
    # Load the CSV file
    with open('data\\4seg_children.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Initialize the parent values list
    parents = []
    nextAvailableID = 0
    children = []
     # Loop through number of population size
    for i in range(0, c.populationSize):
        parents.append(rows[i])
        nextAvailableID += 1

    for i in range(0, len(rows)):
        children.append(rows[i])
        nextAvailableID += 1
    
    for i in range(c.numberOfGenerations):
        print(i)
        # Select new parent
        for i in range(len(parents)):
            if parents[i][2] > children[i][2]:
                parents[i] = children[i]
        parents = parents + parents[-c.populationSize:]
    # Print values to a file
    with open('data\\4seg_parents.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(parents)

merge_rows()
# parents()