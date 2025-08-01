import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# Data Loading
mushrooms = pd.read_csv('./data/mushrooms.csv')

# Analyzing mushrooms data: figuring out datapoints, features, columns, datatypes, some statistical datas such as count, unique values, etc
def analyze_data(df):
    pd.set_option('display.max_columns', None)
    print(f'(datapoints, features): {df.shape}')
    print('-----------------------')
    print(f'Columns: {df.columns}')
    print('-----------------------')
    print(f'Some more detailed info:')
    df.info()
    print('-----------------------')
    print(f"First few rows:\n{df.head()}")
    print('-----------------------')
    print(f'Last few rows:\n{df.tail()}')
    print('-----------------------')
    print(f'Statistical information about the data:\n{df.describe()}')
    print('-----------------------')
    print('-----------------------')

# Preprocessing the data
# Convert class column to category
cols = mushrooms.select_dtypes(['object']).columns
mushrooms[cols] = mushrooms[cols].astype('category')
edibleclass = mushrooms.groupby(['class']).count()
print(edibleclass)

# Data Visualization
# Draw a Pie Chart: mushroom population
def draw_pie_population():
    edibleclass = mushrooms.groupby(['class']).count()
    print(edibleclass)
    labels = ['Edible', 'Poisonous']
    plt.pie(edibleclass['population'], labels=labels, autopct='%.1f %%')
    plt.title('Edible?')


# Draw a donut chart: mushroom habitat
def draw_donut_habitat():
    habitat = mushrooms.groupby(['habitat']).count()
    print(habitat)
    labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']
    # draw a chart and a center circle, then adds that center circle in the chart
    plt.pie(habitat['class'], labels=labels, autopct='%1.1f%%', pctdistance=0.85)

    center_circle = plt.Circle((0,0), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.title('Mushroom Habitats')

# Draw a waffle chart: visualizing the different quantities of mushroom cap colors in this dataset
def draw_waffle_mushroom_capcolors():
    cap_colors = mushrooms.groupby(['cap-color']).count()
    print(cap_colors)
    data = { 'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
            'amount': cap_colors['class']}
    df = pd.DataFrame(data)

    fig = plt.figure(
        FigureClass=Waffle,
        rows=100,
        values= df.amount,
        labels= list(df.color),
        figsize=(30,30),
        colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
    )

draw_waffle_mushroom_capcolors()
plt.show()