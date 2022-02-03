import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('https://raw.githubusercontent.com/cs573-22s/a2-DataVis-5ways/main/cars-sample.csv')
sb.set(rc={'figure.figsize':(6,5)})
scatter = sb.scatterplot(
    data=df,
    x='Weight',
    y='MPG',
    hue='Manufacturer',
    size='Weight',
    alpha=0.5,
    palette=['#d52020', '#d5b820', '#d1d520', '#96d520', '#20d5a4']
)
plt.legend(fontsize='x-small')
plt.show()