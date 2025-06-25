import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Find mean and standard deviation and plot hostogram from randomly generated sample space of 30 numbers with uniform distribution from 0 to 9
def find_mean_and_sd_and_plot_histogram():
    samples = [ random.randint(0,10) for _ in range(30)]
    #samples = [1, 0, 1, 5, 2, 0, 1, 2, 2, 5, 1, 2, 1, 3, 2, 1, 2, 1, 2, 2, 3, 0, 0, 3, 2, 1, 2, 1, 0, 2]
    print(f'Sample: {samples}')
    print(f'Mean: {np.mean(samples)}')
    print(f'Variance: {np.var(samples)}')

    plt.hist(samples)
    plt.show()

# Analyzing Read Data: of baseball players
# Compute mean, variance, standard deviation, median value, quartiles and visualize them using a box plot
def analyze_baseball_players_height():
    df = pd.read_csv("data/SOCR_MLB.tsv", sep='\t', header=None, names=['Name','Team','Role','Height','Weight','Age'])

    # Compute average values of age, height and weight
    avg = df[['Age', 'Height', 'Weight']].mean()
    print(avg)

    # Compute mean, median, Standard Deviation and Variance of Height
    print(list(df['Height'])[:20])
    mean = df['Height'].mean()
    var = df['Height'].var()
    std = df['Height'].std()
    median = df['Height'].median()
    print(f'Mean: {mean}\nVariance: {var}\nStandard Deviation:{std}\nMedian: {median}')

    df.boxplot(column='Height', by='Role', figsize=(10,8))
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.show()

def compute_test_statistics_temp():
    sample = list([74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 72, 73, 75, 78])
    # Compute mean, median, Standard Deviation and Variance of Height
    print(sample)
    print(np.sort(sample))
    mean = np.mean(sample)
    var = np.var(sample)
    std = np.std(sample)
    median = np.median(sample)
    print(f'Mean: {mean}\nVariance: {var}\nStandard Deviation:{std}\nMedian: {median}')

    plt.figure(figsize=(10,2))
    plt.boxplot(sample, vert=False, showmeans=True)
    plt.grid(color='gray')
    plt.tight_layout()
    plt.show()

# Compute mean, variance, standard deviation, median value, quartiles and visualize them using a box plot
def analyze_baseball_players_weight():
    df = pd.read_csv("data/SOCR_MLB.tsv", sep='\t', header=None, names=['Name','Team','Role','Height','Weight','Age'])

    # Compute average values of age, height and weight
    avg = df[['Age', 'Height', 'Weight']].mean()
    
    # Compute mean, median, Standard Deviation and Variance of Height
    print(list(df['Weight'])[:20])
    mean = df['Weight'].mean()
    var = df['Weight'].var()
    std = df['Weight'].std()
    median = df['Weight'].median()
    print(f'Mean: {mean}\nVariance: {var}\nStandard Deviation:{std}\nMedian: {median}')

    df['Weight'].hist(bins=15, figsize=(10,6))
    plt.suptitle('Weight distribution of MLB Players')
    plt.xlabel('Weight')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
    

analyze_baseball_players_weight()
