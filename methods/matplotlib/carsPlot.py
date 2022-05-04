import matplotlib.pyplot as plt
import pandas as pd
fig, ax = plt.subplots(figsize=(10,6))

df = pd.read_csv('cars-sample.csv')
colors = {'bmw': 'lightblue', 'ford': 'red', 'honda': 'green', 'mercedes': 'orange', 'toyota': 'darkblue'}

scatter = plt.scatter("Weight", "MPG", s=(df["Weight"]/20), data=df, c=df["Manufacturer"].map(colors), alpha=0.5)
plt.title('Cars Sample')
plt.xlabel("Weight (lbs)")
plt.xlim([2000,5000])
plt.ylim([10,40])
plt.ylabel("MPG")

handles2, labels2 = scatter.legend_elements(prop="sizes", alpha=0.5)
sizesLegend = ax.legend(handles2, labels2, loc="lower right", title="Weight/20 lbs")
ax.add_artist(sizesLegend)

plt.show()