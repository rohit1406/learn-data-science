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
    birds['MaxBodyMass'].plot(kind='hist', bins=40, figsize=(12,12))
    plt.title('Full distribution: bodymass < 60, bins=40')
    plt.xlabel('Max Body Mass')
    plt.ylabel('Count')

# Histogram: compare relationship between two distributions: 
# MaxBodyMass vs MaxLength
def compare_distributions():
    filtered_birds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
    x = filtered_birds['MaxBodyMass']
    y = filtered_birds['MaxLength']
    fig, ax = plt.subplots(tight_layout=True)
    hist = ax.hist2d(x,y)

# Histogram: Conservation Status vs MinWingspan
def distribution_using_text_data():
    filtered_birds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]
    x1 = filtered_birds.loc[filtered_birds.ConservationStatus=='EX', 'MinWingspan']
    x2 = filtered_birds.loc[filtered_birds.ConservationStatus=='CR', 'MinWingspan']
    x3 = filtered_birds.loc[filtered_birds.ConservationStatus=='EN', 'MinWingspan']
    x4 = filtered_birds.loc[filtered_birds.ConservationStatus=='NT', 'MinWingspan']
    x5 = filtered_birds.loc[filtered_birds.ConservationStatus=='VU', 'MinWingspan']
    x6 = filtered_birds.loc[filtered_birds.ConservationStatus=='LC', 'MinWingspan']

    kwargs = dict(alpha=0.5, bins=20)

    plt.hist(x1, **kwargs, color='red', label='Extinct')
    plt.hist(x2, **kwargs, color='orange', label='Critically Endangered')
    plt.hist(x3, **kwargs, color='yellow', label='Endnagered')
    plt.hist(x4, **kwargs, color='green', label='Near Threatened')
    plt.hist(x5, **kwargs, color='blue', label='Vulnerable')
    plt.hist(x6, **kwargs, color='gray', label='Least Concern')

    plt.gca().set(title='Conservation Status', ylabel='Min Wingspan')
    plt.legend()

distribution_using_text_data()
plt.show()
