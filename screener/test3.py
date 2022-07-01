# https://datarockie.com/blog/basic-python-pandas/

import pandas as pd

penguins = pd.read_csv("penguins.csv")

# print(penguins.head())
# print(penguins.tail())
# print(penguins.shape)
# print(penguins.info())
# print(penguins.describe())
penguins = penguins.dropna()
#penguins = penguins.reset_index()
# print(penguins)

print(penguins['sex'].head())
penguins = penguins.rename(columns = {'sex':'gender'})
#print(penguins['sex'].head())
print(penguins['gender'].head())

# access data method
# 1. iloc[index] - access via index
print(penguins.iloc[0:5])
# 2. loc[] - filter with condition
print(penguins.loc[ penguins['bill_length_mm'] >= 55])
# 3. query() - filter with condition like loc[]
print(penguins.query("bill_length_mm > 55"))

penguins = penguins.sort_values(by='bill_length_mm', ascending = False)

penguins.to_csv('penguins_output.csv')