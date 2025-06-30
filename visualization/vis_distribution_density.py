import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

birds = pd.read_csv('./data/birds.csv')
filtered_birds = birds[(birds['MaxBodyMass'] > 1) & (birds['MaxBodyMass'] < 60)]

# Draw a basic density plot for MinWingspan
def draw_dp_basic_minwingspan():
    sns.kdeplot(filtered_birds['MinWingspan'])
    plt.title('Density plot: MinWingspan')

# Draw a density plot of MaxBodyMass
def draw_dp_maxbodymass():
    sns.kdeplot(filtered_birds['MaxBodyMass'], bw_adjust=0.2)
    plt.title('Density plot: MaxBodyMass')

draw_dp_maxbodymass()
plt.show()