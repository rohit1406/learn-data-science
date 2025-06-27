import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Getting the data

# Load the data
def load_data():
    base_url = "../cord-19_2020-04-10/2020-04-10/"
    metadata_url = base_url + "metadata.csv"
    df = pd.read_csv(metadata_url)
    return df

df = load_data()

def preprocess_data(df):
    # convert publish_time to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], format='mixed')
    return df

# See COVID paper publications over the years: draws histogram
def see_COVID_publications_over_years(df):
    df['publish_time'].hist()

df = preprocess_data(df) 

# Structured data extraction
# List of possible medications used to treat COVID
medications = ['hydroxychloroquine', 'chloroquine', 'tocilizumab', 'remdesivir', 'azithromycin', 
    'lopinavir', 'ritonavir', 'dexamethasone', 'heparin', 'favipiravir', 'methylprednisolone']
# List of diagnosis
diagnosis = ['covid','sars','pneumonia','infection','diabetes','coronavirus','death']

def analyze_and_add_medications_diagnosis_details():
    for m in medications:
        print(f' + Processing medication: {m}')
        df[m] = df['abstract'].apply(lambda x: str(x).lower().count(' '+m))

    for m in diagnosis:
        print(f' + Processing diagnosis: {m}')
        df[m] = df['abstract'].apply(lambda x: str(x).lower().count(' '+m))

analyze_and_add_medications_diagnosis_details()


dfm = df[medications]
# Find most popular medications
def draw_most_popular_medications():
    dfm = dfm.sum().reset_index().rename(columns={'index': 'Name', 0: 'Count'})
    dfm = dfm.sort_values('Count', ascending=False)
    dfm.set_index('Name').plot(kind='bar')

# Looking for trends in treatment strategy
def compute_publish_time_monthly_trend():
    dfm = df[['publish_time']+medications].set_index('publish_time')
    dfm = dfm[(dfm.index>="2020-01-01") & (dfm.index<="2021-07-31")]
    dfmt = dfm.groupby([dfm.index.year, dfm.index.month]).sum()
    return dfmt

dfmt = compute_publish_time_monthly_trend()

def draw_publish_time_plot():
    dfmt.plot()
    dfmt.plot.area() # Stack plot or area plot (in pandas)


# Compute relative popularity in percent
def compute_popularity_in_precentage():
    dfmtp = dfmt.iloc[:,:].apply(lambda x: x/x.sum(), axis=1)
    return dfmtp

dfmtp = compute_popularity_in_precentage()

def draw_popularity_in_precentage():
    dfmtp.plot.area() # Stack plot or area plot (in pandas)



# Visualize few medicines
def visualize_few_medicines():
    meds = ['hydroxychloroquine','tocilizumab','favipiravir']
    dfmt.loc[(2020,1)] = np.nan
    dfmt.loc[(2021,1)] = np.nan
    dfmt.fillna(method='pad', inplace=True)
    fig, ax = plt.subplots(1, len(meds), figsize=(10,3))
    for i,m in enumerate(meds):
        dfmt[m].plot(ax=ax[i])
        ax[i].set_title(m)

# Computing Medicine-Diagnosis Correspondence
# compute co-occurence frequency map
def compute_medicine_diagnosis_correspondence():
    m = np.zeros((len(medications), len(diagnosis)))
    for a in df['abstract']:
        x = str(a).lower()
        for i,d in enumerate(diagnosis):
            if ' '+d in x:
                for j,me in enumerate(medications):
                    if ' '+me in x:
                        m[j,i] += 1
    return m

m = compute_medicine_diagnosis_correspondence()

# Draw a heatmap
def draw_heatmap_of_correspondence():
    plt.imshow(m, interpolation='nearest', cmap='hot')
    ax = plt.gca()
    ax.set_yticks(range(len(medications)))
    ax.set_yticklabels(medications)
    ax.set_xticks(range(len(diagnosis)))
    ax.set_xticklabels(diagnosis, rotation=90)

draw_heatmap_of_correspondence()

# Draw plotly sankey diagram
def draw_sankey_diagram(cat1, cat2, m, threshold=0, h1=[], h2=[]):
    all_nodes = cat1 + cat2
    source_indices = list(range(len(cat1)))
    target_indices = list(range(len(cat1), len(cat1)+len(cat2)))

    s,t,v,c = [], [], [], []
    for i in range(len(cat1)):
        for j in range(len(cat2)):
            if m[i,j]>threshold:
                s.append(i)
                t.append(len(cat1)+j)
                v.append(m[i,j])
                c.append('pink' if i in h1 or j in h2 else 'lightgray')

    fig = go.Figure(
        data=[
            go.Sankey(
                # Define Nodes
                node = dict(
                    pad = 40,
                    thickness = 40,
                    line = dict(color="black", width=1.0),
                    label = all_nodes
                ),

                # Add links
                link = dict(
                    source = s,
                    target = t,
                    value = v,
                    color = c
                )
            )
        ]
    )
    fig.show()

#draw_sankey_diagram(medications, diagnosis, m, 500, h2=[0])
#pd.set_option('display.max_columns', None)
#print(dfm.head())
plt.show()