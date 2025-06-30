import pandas as pd
import matplotlib.pyplot as plt

# import the data
birds = pd.read_csv('./data/birds.csv')

# draw a scatter plot
def draw_sp_maxlength_per_order():
    birds.plot(kind='scatter', x='MaxLength', y='Order', figsize=(12,8))
    plt.title('Max Length per Order')
    plt.xlabel('Max Length')
    plt.ylabel('Order')
    
draw_sp_maxlength_per_order()
plt.show()