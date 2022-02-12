import matplotlib.pyplot as plt
import pandas
import numpy as np

data = pandas.read_csv("../cars-sample.csv")


fig, ax = plt.subplots()

colors = ["lightcoral", "darkkhaki", "limegreen", "dodgerblue", "mediumorchid"]
x_ticks = np.arange(2000, 6000, 1000)
y_ticks = np.arange(10, 50, 10)

for (manufacturer, group), color in zip(data.groupby(["Manufacturer"]), colors):
    scale = group["Weight"] / 20 - 70
    ax.scatter(group["Weight"], group["MPG"], c=color, s=scale, label=manufacturer,
               alpha=np.sqrt(0.5), edgecolors='none')


ax.set_xlabel("Weight")
ax.set_ylabel("MPG")

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.grid(True)

fig.savefig("out.png")
