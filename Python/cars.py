from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd

#read CSV Pandas
car_data = pd.read_csv('../cars-sample.csv')

ax = plt.axes()
ax.set_facecolor('#EEEEEE')
# for x in car_data:
for index, row in car_data.iterrows():
    if(row[2] == "ford"):
        ax.scatter(row[7], row[3], c="#FFA50080", s=(row[7]*0.05), data=row)
    if(row[2] == "bmw"):
        ax.scatter(row[7], row[3], c="#DD1C1A80", s=(row[7]*0.05), data=row)
    if(row[2] == "honda"):
        ax.scatter(row[7], row[3], c="#F5E40080", s=(row[7]*0.05), data=row)
    if(row[2] == "mercedes"):
        ax.scatter(row[7], row[3], c="#8E7CA280", s=(row[7]*0.05), data=row)
    if(row[2] == "toyota"):
        ax.scatter(row[7], row[3], c="#0000FF80", s=(row[7]*0.05), data=row)
ax.scatter(0, 0, s=0, c="#000000", label="Manufacturer")
ax.scatter(0, 0, s=50, c="#FFA50080", label="Ford")
ax.scatter(0, 0, s=50, c="#DD1C1A80", label="BMW")
ax.scatter(0, 0, s=50, c="#F5E40080", label="Honda")
ax.scatter(0, 0, s=50, c="#8E7CA280", label="Mercedes")
ax.scatter(0, 0, s=50, c="#0000FF80", label="Toyota")
ax.scatter(0, 0, s=0, c="#000000", label="Weight")
ax.scatter(0, 0, s=2000*0.05, c="#000000", label="2000")
ax.scatter(0, 0, s=3000*0.05, c="#000000", label="3000")
ax.scatter(0, 0, s=4000*0.05, c="#000000", label="4000")
ax.legend()
for index, tick in enumerate(ax.xaxis.get_ticklabels()):
    if index % 2 != 0:
        tick.set_visible(False)
for index, tick in enumerate(ax.yaxis.get_ticklabels()):
    if index % 2 != 1:
        tick.set_visible(False)  
plt.xlabel('Weight')
plt.ylabel('MPG')
# plt.style.context('ggplot')
ax.grid(color='#FFFFFF', linestyle='solid', markeredgecolor ='#FFFFFF')
plt.show()