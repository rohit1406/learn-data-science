import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
honey = pd.read_csv('./data/honey.csv')

# draw Scatter plot: show relationship between the price per pound of honey and its US state of origin
def draw_sp_ppp_vs_state():
    sns.relplot(x='priceperlb', y='state', data=honey, height=5, aspect=0.5)
    plt.title('State vs Price Per Pound')

# draw Scatter plot: show PPP vs origin State with color scheme
def draw_sp_ppp_vs_state_colored():
    sns.relplot(x='priceperlb', y='state', data=honey, hue='year', palette='YlOrBr', height=5, aspect=0.5)
    plt.title('State vs Price Per Pound with Color')

# draw Scatter plot: show PPP vs origin State with size
def draw_sp_ppp_vs_state_sized():
    sns.relplot(x='priceperlb', y='state', data=honey, size='year', palette='YlOrBr', height=5, aspect=0.5)
    plt.title('State vs Price Per Pound with Size')

# Is there a clear rise in price of honey per pound year over year?
# Plot a line chart
def draw_lc_ppp_year():
    sns.relplot(x="year", y="priceperlb", data=honey, kind='line')
    plt.title('Progression of Price Per Pound over the years')

# Check supply of honey
def draw_lc_ppp_year():
    sns.relplot(x="year", y="totalprod", data=honey, kind='line')
    plt.title('Honey Production over the years')

draw_lc_ppp_year()
plt.show()