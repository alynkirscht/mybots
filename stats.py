import pandas as pd
from scipy.stats import spearmanr

# read the data from the CSV files
x_data = pd.read_csv('data\\angleAxisRandom.csv')
y_data = pd.read_csv('data\\angleAxis20Gen.csv')

for i in range(6):
    if (i == 5):
        corr, pval = spearmanr(x_data['Fitness'], y_data['Fitness'])
    else:
        corr, pval = spearmanr(x_data['Joint ' + str(i+1)], y_data['Joint ' + str(i+1)])
    print(f"Spearman correlation coefficient between column {i+1} in random snakes and column {i+1} in  30 gen evolved snakes: {corr:.3f}")
    print(f"p-value: {pval:.3f}")



