import pandas as pd
import matplotlib.pyplot as plt

# import the data
birds = pd.read_csv('./data/birds.csv')

# draw a scatter plot to show distribution of max length per bird order
def draw_sp_maxlength_per_order():
    birds.plot(kind='scatter', x='MaxLength', y='Order', figsize=(12,8))
    plt.title('Max Length per Order')
    plt.xlabel('Max Length')
    plt.ylabel('Order')

# Histogram showing full distribution
def draw_hist_maxbodymass():
    filtered_birds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
    filtered_birds.plot(kind='hist', bins=40, figsize=(12,12))
    plt.title('Full distribution: bodymass < 60, bins=40')
    plt.xlabel('Max Body Mass')
    plt.ylabel('Count')

draw_hist_maxbodymass()
plt.show()