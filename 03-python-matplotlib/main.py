import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pandas

plt.style.use('seaborn')

# colorscheme based on d3 categorical swatches
colorscheme = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
               "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]

df = pandas.read_csv("cars-sample.csv")
manufacturers = df['Manufacturer'].unique().tolist()
manufacturers.sort()

mpg = df['MPG']
weight = df['Weight']

min_size = df['Weight'].min()
max_size = df['Weight'].max()
size = ((df['Weight'] - min_size) / (max_size-min_size) * 150 + 50)

colors_map = {manufacturer: colorscheme[idx]
              for idx, manufacturer in enumerate(manufacturers)}

colors = df['Manufacturer'].map(colors_map)


fig, ax = plt.subplots()

manufacturers_handles = [mpatches.Patch(
    color=colors_map[key], label=key) for key in colors_map]
l1 = ax.legend(handles=manufacturers_handles, loc="upper right", title="Manufacturer")



scatter = ax.scatter(weight, mpg, s=size, c=colors, alpha=0.5)

kw = dict(prop="sizes", num=4, color='#777',
          func=lambda s: (s - 50) * (max_size - min_size) / 150 + min_size)
l2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="center right", title="Weight")


ax.add_artist(l1)
ax.add_artist(l2)
plt.show()

