import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cars-sample.csv")
weight = data['Weight']
mpg = data['MPG']
manufacturer = data['Manufacturer']

color_dict = { 'bmw':'pink', 'ford':'olive', 'honda':'green', 'mercedes':'blue','toyota':'purple' }


plt.scatter(weight,mpg, color=[ color_dict[i] for i in manufacturer], alpha=0.5, s=weight/25)

plt.title('Python Graph')
plt.xlabel('Weight')
plt.ylabel('MPG')

plt.show()