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

# Draw a MaxBodyMass density per bird Order
def draw_dp_maxbodymass_per_order():
    sns.kdeplot(filtered_birds, x='MaxBodyMass', hue='Order',
                fill=True, common_norm=False, palette='crest',
                alpha=0.5, linewidth=0)
    plt.title('Density plot: MaxBodyMass per bird Order')

# Map the density of several variables (MaxLength, MinLength of birds) in one chart
def draw_dep_map_several_var():
    sns.kdeplot(data=filtered_birds, x='MinLength', y='MaxLength', hue="ConservationStatus")
    plt.title('Density plot: map MaxLength and MinLength in single chart')

draw_dep_map_several_var()
plt.show()