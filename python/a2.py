import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df=pd.read_csv('/Users/yujunmao/Desktop/CS573_A2/cars-sample.csv')

sb.set(rc={'figure.figsize':(6,5)})

# plot
scatter = sb.scatterplot(
    data=df,
    x='Weight',
    y='MPG',
    hue='Manufacturer',
    size='Weight',
    alpha=0.5,
    palette=["#999999", "#E69F00", "#56B4E9", "#C71585", "#4B0082"]
)
plt.legend(fontsize='x-small')
plt.show()