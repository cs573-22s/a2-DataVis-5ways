import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("../cars-sample.csv")
print(data.columns)
sns.set_style("darkgrid")
sns.scatterplot(x=data.Weight, y=data.MPG, 
    size=data.Weight, hue=data.Manufacturer, alpha=0.5,
    sizes=(15, 200), palette="muted")
plt.savefig("fig.png")
print(data)