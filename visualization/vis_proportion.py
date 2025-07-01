import pandas as pd
import matplotlib.pyplot as plt

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

analyze_data(mushrooms)