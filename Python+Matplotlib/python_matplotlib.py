from cProfile import label
from logging import handlers
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
size = size**2*80
print(size)

# color
colorset = ['#FAB9AC','#7BBC53','#DE6736','#67C1EC','#E6B90D']
color = []
for i in data.index:
    for j in range(0, len(Manufacturer_type)):
        if data['Manufacturer'][i] == Manufacturer_type[j]:
            color.append(colorset[j])
print(color)

# plot

plt.rcParams['axes.facecolor'] = '#ECECEC'
plt.grid(c='w')


plt.scatter(Weight,MPG, s=size, c=color, alpha=0.5, zorder=2)


plt.xlabel('Weight')
plt.ylabel('MPG')

ax = plt.gca()
ax.spines['left'].set_color('#ECECEC')
ax.spines['right'].set_color('#ECECEC')
ax.spines['top'].set_color('#ECECEC')
ax.spines['bottom'].set_color('#ECECEC')

for size in [2000, 3000, 4000]:
    s = size / (weight_max - weight_min)
    s = s**2*80
    plt.scatter([],[],c='#878787', s=s, label=str(size))
l1 = plt.legend(bbox_to_anchor=(1.05, 0.5), loc='upper left', scatterpoints=1, labelspacing=0.5, title='Weight')


color_handles = [mpatches.Patch(color=colorset[i], alpha=0.5, label=Manufacturer_type[i]) for i in range(0,5)]
plt.legend(handles=color_handles, bbox_to_anchor=(1.05, 0.9), loc='upper left', scatterpoints=1, labelspacing=0.5, title='Manufacturer')

ax.add_artist(l1)

plt.tight_layout()
plt.show()
          



