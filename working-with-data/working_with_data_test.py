import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Analyze sales of our ice-creame shop
def analyze_sales_within_date_range():
    start_date = "Jan 1, 2020"
    end_date="Mar 31, 2020"
    idx = pd.date_range(start_date, end_date)
    print(f'Length of index is {len(idx)}')

    items_sold = pd.Series(np.random.randint(25, 50, size=len(idx)), index=idx)
    print(f'Items Sold:\n{items_sold.head()}')
    additional_items = pd.Series(10, index=pd.date_range(start_date, end_date, freq='W'))
    print(f'Additional Items: (10) items each week\n{additional_items}')
    total_sold = items_sold.add(additional_items, fill_value=0)
    print(f'Total items - {len(total_sold)} (sum of two series):\n{total_sold}')
    total_sold.plot(figsize=(10,3))
    # plt.show()

    # Resampling: monthly
    monthly = total_sold.resample("ME").mean()
    ax = monthly.plot(kind='bar', figsize=(10, 6))
    ax.set_xticklabels([x.strftime("%b-%Y") for x in monthly.index], rotation=45)
    plt.show()

# DataFrame meaning:: Collection of Series
# Print DataFrames in rows, columns and perform transpose operation to DataFrame
def working_with_data_frames():
    a = pd.Series(range(0, 10))
    b = pd.Series(["I","like","to","play","games","and","will","not","change"], index=range(1, 10))
    # Create Data Frames as rows
    df_rows = pd.DataFrame([a,b])
    print(df_rows)

    # Create DataFrames as columns
    df_columns = pd.DataFrame({'A': a, 'B': b})
    print(df_columns)

    # Transpose the layout
    # .T means the operation of transposing the DataFrame i.e. changing rows and columns
    # rename operation allows us to rename columns
    df_transpose = pd.DataFrame([a,b]).T.rename(columns={0: 'A', 1: 'B'})

    # Selecting columns from dataframe
    print(f'Column A(Series):\n{df_transpose['A']}')
    print(f'Column B and A:\n{df_transpose[['B','A']]}')
    print(f'Selection Based on Filter >5 and <8\n{df_transpose[(df_transpose['A']>5) & (df_transpose['A']<8)]}')
    
    # Create a new computable column
    # DivA - calculates divergence of A from it's mean value
    df_transpose['DivA'] = df_transpose['A']-df_transpose['A'].mean()
    df_transpose['LenB'] = df_transpose['B'].fillna('n/a').apply(lambda x: len(x))
    #df_transpose.plot()
    #plt.show()
    df = df_transpose[['A']]
    df.plot(kind='bar')
    print(df)
    plt.show()

def working_with_series():
    # Integer Series
    a = pd.Series(range(1, 10))
    # String Series
    b = pd.Series(["I","like","to","see","you!"], index=range(1, 6))
    print(a,b)

# series()
# analyze_sales()
working_with_data_frames()