import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv

MPG = []
Weight = []
BubbleWeight = []
Manufacturer = []

def numericManufacturer(m):
    if m == 'bmw':
        return "#FF69B4"
    elif m == 'ford':
        return "#00BFFF"
    elif m == 'honda':
        return "#32CD32"
    elif m == 'mercedes':
        return "#FFFF00"
    else:
        return "#808080"

with open("cars-sample.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ',')
    for row in csv_reader:
        # skip the rows with no MPG values
        if row['MPG'] != 'NA':
            MPG.append(float(row['MPG']))
            Weight.append(float(row['Weight']))
            BubbleWeight.append(float(row['Weight'])*0.03)
            Manufacturer.append(numericManufacturer(row['Manufacturer']))

fig, ax = plt.subplots()
scatter = ax.scatter(Weight, MPG, s = BubbleWeight, c = Manufacturer, alpha = 0.5)
ax.set_ylabel('MPG')
ax.set_xlabel('Weight')
plt.grid(color = '#ECECEC')

classes = ['bmw','ford','honda','mercedes','toyota']
class_colours = ['#FF69B4','#00BFFF','#32CD32','#FFFF00','#808080']
recs = []
for i in range(0, len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc = class_colours[i]))
colorLegend = ax.legend(recs, classes, loc = 'upper right')

ax.add_artist(colorLegend)

handles, labels = scatter.legend_elements(prop = "sizes", alpha = 0.5, num = 4)
handles.pop(3)
labels = ['$\\mathdefault{2000}$', '$\\mathdefault{3000}$', '$\\mathdefault{4000}$']
weightLegend = ax.legend(handles, labels, title = "Weight",loc = (0.81,0.43))

plt.show()