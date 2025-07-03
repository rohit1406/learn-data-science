import pandas as pd
import glob

# Loading the dataset
emails_df = pd.read_csv('./data/emails.csv')
print(emails_df.describe())

# Sampling 10 emails
print(emails_df.sample(10))

# Returns rows where there are more occurences of "to" than "the"
print(emails_df.query('the < to'))