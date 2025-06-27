import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make figures broader
plt.rcParams["figure.figsize"] = (10,3)

## Loading the data: 
# get infected, recovered and deaths related COVID19 data across the globe
# also get the countries data such as population
def get_covid19_spread_data():
    # loading data from the internet
    base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
    # loading data from the local disk
    #base_url = "../data/COVID/"
    infected_dataset_url = base_url + "time_series_covid19_confirmed_global.csv"
    recovered_dataset_url = base_url + "time_series_covid19_recovered_global.csv"
    deaths_dataset_url = base_url + "time_series_covid19_deaths_global.csv"
    countries_dataset_url = base_url + "../UID_ISO_FIPS_LookUp_Table.csv"

    # Load the data
    infected = pd.read_csv(infected_dataset_url)
    recovered = pd.read_csv(recovered_dataset_url)
    deaths = pd.read_csv(deaths_dataset_url)
    countries = pd.read_csv(countries_dataset_url)

    ## Pre-processing data
    # Get information on whole country instead of per province
    infected = infected.groupby('Country/Region').sum()
    recovered = recovered.groupby('Country/Region').sum()
    deaths = deaths.groupby('Country/Region').sum()

    # Drop colums Province/State, Lat, Long
    infected.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    recovered.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    deaths.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)

    ## Visualizing the data: plot the data on graph
    #infected.loc['India'][3:].plot()
    #recovered.loc['India'][3:].plot()
    #deaths.loc['India'][3:].plot()
    #plt.show()
    return (infected, recovered, deaths, countries)

# Create a frame that contains the data on infections indexed by date
def mkframe(country):
    df = pd.DataFrame({
        'infected': infected.loc[country],
        'recovered': recovered.loc[country],
        'deaths': deaths.loc[country]
    })
    df.index = pd.to_datetime(df.index)
    return df


# Investigate the data: finding infected, newly infected, percentage of the population, basic reproductive number etc
def analyze_data(country):
    df = mkframe(country)
    # Calculate new infected
    df['ninfected'] = df['infected'].diff()

    # Plot data of specific month
    #df[(df.index.year==2020) & (df.index.month==7)]['ninfected'].plot()
    # Smoothen the curve to see the trends: for each day we will calculate the average value of the previous several days
    df['ninfav'] = df['ninfected'].rolling(window=7).mean()

    # Find population
    pop = countries[(countries['Country_Region']==country) & (countries['Province_State'].isna())]['Population'].iloc[0]
    df['pinfected'] = df['infected']*100 / pop

    # Find Rt
    # R0 is the basic reproductive number which indicates the number of people that an infected person would further infect
    df['Rt']=df['ninfected'].rolling(8).apply(lambda x: x[4:].sum()/x[:4].sum())
    # Replace NaN and inf values
    #ax = df[df.index<'2020-05-01']['Rt'].replace(np.inf, np.nan).fillna(method='pad').plot(figsize=(10,3))
    #ax.set_ylim([0,6]) # Limit y axis values to show values below 6
    # Plot a doted line on 1 parallel to x-axis
    #ax.axhline(1, linestyle='--', color='red')

    # Find daily difference in new cases: this helps us to see clearly when pandemic is increasing or decreasing
    #df['ninfected'].diff().plot()
    # Smoothen the curve
    #ax=df[df.index<"2020-06-01"]['ninfected'].diff().rolling(7).mean().plot()
    #ax.axhline(0,linestyle='-.',color='red')
    plt.show()
    return df


# Load the data of Epidemic spread of COVID-19
(infected, recovered, deaths, countries) = get_covid19_spread_data()

## Investigating the data
country = 'US'
df = analyze_data(country)
print(df)
