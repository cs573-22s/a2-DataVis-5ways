import pandas as pd
import matplotlib.pyplot as plt
from sympy import principal_branch

# read data
data = pd.read_csv('cars-sample.csv')

# data info
print(data.columns)

# check null value
print(data.isnull().any())

data.dropna(axis=0, how='any', inplace=True)

print(data.isnull().any())

# data
Weight = data['Weight']
MPG = data['MPG']
Manufacturer = data['Manufacturer']
Manufacturer_type = data['Manufacturer'].unique().tolist()

# range of weight
weight_min = Weight.min()
weight_max = Weight.max()

print(weight_max)
print(weight_min)

# size of scatter
size = Weight / (weight_max - weight_min)
# check size
print(size)
size = size*20
print(size)




