import pandas as pd
import plotly.express as px

import math

data = pd.read_csv("./cars-sample.csv")
sorted = data.sort_values("Manufacturer")
print(sorted)

fig = px.scatter(sorted, x='Weight', y='MPG', color='Manufacturer', size='Weight', size_max=30,
                 hover_name='Manufacturer')
fig.update_yaxes(dtick=10)
fig.update_layout(legend= {'itemsizing': 'trace'})
fig.show()

print(data)
