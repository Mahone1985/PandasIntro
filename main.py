# Data Manipulation and Report Building example

# Import your required libraries
import numpy as py
import pandas as pd

# Import your CSV database
data = pd.read_csv(r'./test-files/electronic-card-transactions-april-2023-csv-tables.csv')
df = pd.DataFrame(data, columns=['Period', 'Data_value', 'Series_title_2'])
print(df)
print("***************************************************************************************************")

# Let's do a frequency of the series title 2 field
freqx = df['Series_title_2'].value_counts().sort_index()
freqy = pd.DataFrame({
    'Series_title_2': freqx.index,
    'Frequency': freqx.values,
    'Percent': ((freqx.values/freqx.values.sum())*100).round(2)
})
print(freqy)
print("***************************************************************************************************")

# Now do a summary of the data value (amount) vs the series title
df_grouped = df.groupby(["Period", "Series_title_2"])["Data_value"].sum()
print(df_grouped)
print("***************************************************************************************************")

# Output your table to a CSV for monitoring
df_grouped.to_csv('./test-files/df_grouped.csv')

# Now we want to try an SQL joining equivalent. Bring in another table of data for comparing
busdata = pd.read_csv(r'./test-files/business-price-indexes-september-2022-quarter-csv.csv')

# Select distinct example
unique_df = df.Series_title_2.unique()
print(unique_df)
print("***************************************************************************************************")
# Project uploaded to Git for the first time

# Let's try a left join. We'll use a bit of a simpler dataset for this
# Create two separate tables that can be joined together

py.random.seed(0)
# transactions
left_df = pd.DataFrame({'transaction_id': ['A', 'B', 'C', 'D'],
                       'user_id': ['Peter', 'John', 'John', 'Anna'],
                       'value': py.random.randn(4),
                      })
# users
right_df = pd.DataFrame({'user_id': ['Paul', 'Mary', 'John',
                                     'Anna'],
                        'favorite_color': ['blue', 'blue', 'red',
                                           py.NaN],
                       })
# left join user_id
left_joined = left_df.merge(right_df.rename({'user_id': 'user_id_r'}, axis=1),
               left_on='user_id', right_on='user_id_r', how='left')

# output resulting dataset
left_joined.to_csv('./test-files/left_joined.csv')

