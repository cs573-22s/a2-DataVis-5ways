import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('D:/CS573/A2/cars.csv')

#print(df)

sb.set(rc={'figure.figsize':(6,5)})

# plot
scatter = sb.scatterplot(
    data=df,
    x='Weight',
    y='MPG',
    hue='Manufacturer',
    size='Weight',
    alpha=0.5,
    palette=['#a3a500', '#e76bf3', '#f8766d', '#00bf7d', '#00b0f6']
)
plt.legend(fontsize='x-small')
plt.show()