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

# Try to find out answer for below questions:
# What other influences in the data could affect the tip amount?
# What columns will most likely not be needed to answer the client's questions?
# Based on what has been provided so far, does the data seem to provide any evidence of seasonal tipping behavior?
def analyzing_taxi_data():
    # Find trip duration
    taxi['trip_duration'] = taxi['tpep_dropoff_datetime'] - taxi['tpep_pickup_datetime']
    # Plot distribution of trip duration
    #taxi.plot(kind='scatter', x='trip_duration', y='index', figsize=(8,12))
    #print(taxi.head())
    # TODO: coming soon

preprocess_taxi_data()
analyzing_taxi_data()
plt.show()