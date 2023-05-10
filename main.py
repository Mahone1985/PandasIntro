# Data Manipulation and Report Building example

# Import your required libraries
import numpy as py
import pandas as pd

# Import your CSV database
data = pd.read_csv(r'/home/dodonpachi85/Downloads/electronic-card-transactions-april-2023-csv-tables.csv')
df = pd.DataFrame(data, columns=['Period', 'Data_value', 'Series_title_2'])
print(df)

# Let's do a frequency of the series title 2 field
freqx = df['Series_title_2'].value_counts().sort_index()
freqy = pd.DataFrame({
    'Series_title_2': freqx.index,
    'Frequency': freqx.values,
    'Percent': ((freqx.values/freqx.values.sum())*100).round(2)
})
print(freqy)

# Now do a summary of the data value (amount) vs the series title
df_grouped = df.groupby(["Period", "Series_title_2"])["Data_value"].sum()
print(df_grouped)

# Output your table to a CSV for monitoring
df_grouped.to_csv('/home/dodonpachi85/Downloads/df_grouped.csv')

# Now we want to try an SQL joining equivalent. Bring in another table of data for comparing
busdata = pd.read_csv(r'/home/dodonpachi85/Downloads/business-price-indexes-september-2022-quarter-csv.csv')

# Select distinct example
unique_df = df.Series_title_2.unique()
print(unique_df)

# Project uploaded to Git for the first time

