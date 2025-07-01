import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
honey = pd.read_csv('./data/honey.csv')
print(honey[honey['state']=='AL'])
# draw Scatter plot: show relationship between the price per pound of honey and its US state of origin
def draw_sp_ppp_vs_state():
    sns.relplot(x='priceperlb', y='state', data=honey, height=5, aspect=0.5)
    plt.title('State vs Price Per Pound')

draw_sp_ppp_vs_state()
plt.show()