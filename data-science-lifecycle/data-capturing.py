# Defining the purpose and problem that need to be addressed:
# Goal: to investigate a taxi customers seasonal spendings in New York City.
# Purpose: to identify when does yellow taxi customers in New Your City tip drivers more. Whether in Summer or Winter?
# This problem is not solved before. So the outcome will help in any future similar requirements.
# There is No ambiguity in goal and purpose.
# End potential result will look like a bar chart.
# Resources (time, people, computational) are available.

# Next, Identify, collect, evaluate (quantity and quality of data) and explore the data
# This requires some data exploration to confirm what has been acquired will support reaching the desired result.

# Identify: what data is already available to me? -> taxi.csv
# Who owns it: NYC Taxi & Limousine Commission -> https://docs.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets
# Privacy Concerns? : No, Data is available for public use.
import pandas as pd
import matplotlib.pyplot as plt

# Collect the data
taxi = pd.read_csv('./data/taxi.csv')

# Evaluate quantity and quality of data:
# Do I have enough to solve the problem?
# Is the data of acceptable quality for this problem?
# If I discover additional information through this data, should we consider changing or redefining the goals?
def evaluate_taxi_data():
    print(f'(datapoints, features): {taxi.shape}')
    print(f'columns: {taxi.columns}')
    print('--------------------------------------')
    taxi.info()
    print('------------------------------------')
    # Display all the columns of the dataset
    pd.set_option('display.max_columns', None)
    print(f'First five rows:\n{taxi.head()}')
    print(f'Last five rows:\n{taxi.tail()}')
    print('--------------------------')

# Findings:
# date time is object and needs to convert to datetime
# we need to derive season based on month from datetime
def derive_season(month):
    if ( month >= 6 and month <= 8):
        return 'SUMMER'
    elif (month == 12 or (month>=1 and month<=3)):
        return 'WINTER'

def preprocess_taxi_data():
    # Converting object to datetime
    taxi['tpep_pickup_datetime'] = pd.to_datetime(taxi['tpep_pickup_datetime'])
    taxi['tpep_dropoff_datetime'] = pd.to_datetime(taxi['tpep_dropoff_datetime'])
    
    # Derive seasons based on month value from the dataset
    taxi['season'] = taxi['tpep_pickup_datetime'].dt.strftime('%m').apply(lambda x: derive_season(int(x)))

# Visualize taxi data per season
def visualize_taxi_data():
    tip_taxi = taxi.groupby(by='season')['tip_amount'].sum()
    tip_taxi.plot(kind='bar')
    plt.title('Tips given by Customers to Driver per Season')
    plt.xlabel('Season')
    plt.ylabel('Tip Amount')
    plt.xticks(rotation=45)

evaluate_taxi_data()
preprocess_taxi_data()
visualize_taxi_data()
plt.show()