import pandas as pd
import matplotlib.pyplot as plt

# a Line plot about bird wingspan values
birds = pd.read_csv('./data/birds.csv')
wingspan = birds['MaxWingspan']

def draw_basic_line_plot():
    wingspan.plot()


# Draw a basic line plot with labelling x,y axis
def plot_xy_labels_with_rotation():
    plt.title('Max Wingspan in Centimeters')
    plt.ylabel('Wingspan (cm)')
    plt.xlabel('Birds')
    plt.xticks(rotation=45)
    x = birds['Name']
    y = birds['MaxWingspan']
    plt.plot(x,y)


# plot scatter chart with labelling only outliners
def plot_scatter_chart():
    plt.title('Max Wingspan in Centimeters')
    plt.ylabel('Wingspan (cm)')
    plt.xlabel('Birds')
    # hide bottom labels
    plt.tick_params(axis='both', which='both', labelbottom=False, bottom=False)
    for i in range(len(birds)):
        x = birds['Name'][i]
        y = birds['MaxWingspan'][i]
        # Plotting the chart with a small round blue dots
        # Filter 'Bald eagle', 'Prairie falcon' as those holds bad data
        if birds['Name'][i] not in ['Bald eagle', 'Prairie falcon']:
            #plt.text(x, y * (1 - 0.05), birds['Name'][i], fontsize=12)
            plt.plot(x,y,'bo')
            

# Plot a bar chart based on Category
birds.plot(x='Category', kind='bar', stacked=True, title='Birds of Minnesota')
plt.show()