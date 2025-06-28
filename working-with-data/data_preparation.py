import pandas as pd
from sklearn.datasets import load_iris

# Load and Explore iris data: British biologist Ronald Fisher's Iris data set used in his 1936 paper "The use of multiple measurements in taxonomic problems"
def load_and_explore_iris_data():
    print('loading iris data')
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

    # prints (150, 4) -> 150 Datapoints containing 4 Features
    datapoints, features = iris_df.shape
    print(f'dealing with {datapoints} datapoints (rows) and {features} features (columns)')

    # column details
    print(f'column details: {iris_df.columns}')

    # further detailed information about the dataset
    print('further details about the dataset:')
    iris_df.info()
    print(f'statistical summary of numerical columns of the dataset:\n{iris_df.describe()}')

    # print few rows of data
    print(iris_df.head(n=8))
    print(iris_df.tail())

# Load and Explore Iris Data
#load_and_explore_iris_data()