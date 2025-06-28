import pandas as pd
from sklearn.datasets import load_iris
import numpy as np

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


# Dealing with missing data
def missing_data_handling_in_Series():
    # Working with Series
    example3 = pd.Series([0, np.nan, '', None])
    print(example3)
    # find count of null values
    print(example3.isnull().sum())

    # indexing on masked values
    print(example3[example3.notnull()])

    # here output is same as above but difference is here removing missing values
    example3 = example3.dropna() # remove missing/null values
    print(example3)

def missing_data_handling_in_dataframes():
    # Working with DataFrames
    example4 = pd.DataFrame([
        [1, np.nan, 7],
        [2, 5, 8],
        [np.nan, 6, 9]
    ])
    print(example4)
    print(example4.dropna())
    print(example4.dropna(axis="columns"))

    example4[3] = np.nan
    print(example4)
    # Drop only column 3 whose all values are NAN
    print(example4.dropna(axis="columns", how="all"))
    # Set the number of non-null values that a row or column needs to have in order to be kept
    print(example4.dropna(axis="rows", thresh=3))

    # replacing nulls
    print(example4)
    print(example4.fillna(method='ffill', axis=1))
    print(example4.fillna(method='ffill'))
    print(example4.fillna(example4.mean()))

# dealing with categorical data (non-numeric) and numberic such as Gender, True/False, etc
def handling_categorial_nulls():
    # categorical data (non-numeric)
    fill_with_mode = pd.DataFrame([[1,2,"True"],
                               [3,4,None],
                               [5,6,"False"],
                               [7,8,"True"],
                               [9,10,"True"]])
    print(fill_with_mode)
    # See the 'mode' of the values
    print(fill_with_mode[2].value_counts())
    # replace null's with 'mode' i.e. True as we see above
    fill_with_mode[2].fillna("True", inplace=True)
    print(fill_with_mode)
    print('----------------')
    # Numeric
    # Filling with mean
    fill_with_mean = pd.DataFrame([[-2,0,1],
                               [-1,2,3],
                               [np.nan,4,5],
                               [1,6,7],
                               [2,8,9]])
    print(fill_with_mean)
    print(np.mean(fill_with_mean[0]))
    # Filling nulls with mean
    fill_with_mean[0].fillna(np.mean(fill_with_mean[0]), inplace=True)
    print(fill_with_mean)
    print('-------------')
    
    # Filling with median
    fill_with_median = pd.DataFrame([[-2,0,1],
                               [-1,2,3],
                               [0,np.nan,5],
                               [1,6,7],
                               [2,8,9]])
    print(fill_with_median)
    fill_with_median[1].fillna(fill_with_median[1].median(), inplace=True)
    print(fill_with_median)
    print('-------------------')

    # Another example
    example5 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
    print(example5)
    # fill with 0
    print(example5.fillna(0))
    print(example5.fillna(method='bfill'))

# Encoding Categorical Data: Encoding is done to convert non-numeric data to numeric data
def encode_categorical_data():
    # Label encoding
    label = pd.DataFrame(
        [
            [10,'business class'],
            [20,'first class'],
            [30, 'economy class'],
            [40, 'economy class'],
            [50, 'economy class'],
            [60, 'business class']
        ], columns=['ID', 'class']
    )
    print(label)
    # Perform label encoding
    class_labels = {'business class':0, 'economy class':1, 'first class': 2}
    label['class'] = label['class'].replace(class_labels)
    print(label)

    # ONE HOT ENCODING
    one_hot = pd.DataFrame(
        [
            [10,'business class'],
            [20,'first class'],
            [30, 'economy class'],
            [40, 'economy class'],
            [50, 'economy class'],
            [60, 'business class']
        ], columns=['ID', 'class']
    )
    print(one_hot)
    # Perform one hot encoding
    one_hot_data = pd.get_dummies(one_hot, columns=['class'])
    print(one_hot_data)

# Dealing with duplicates
def handling_duplicates():
    example6 = pd.DataFrame({
        'letters': ['A', 'B'] * 2 + ['B'],
        'numbers': [1,2,1,3,3]
    })
    print(example6)
    print(example6.duplicated())
    print(example6.drop_duplicates())
    print(example6.drop_duplicates('letters'))

handling_duplicates()