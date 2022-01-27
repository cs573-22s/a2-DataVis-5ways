import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

from plotly.validators.layout import legend

data = pd.read_csv("./cars-sample.csv")
sorted = data.sort_values("Manufacturer")
print(sorted)


# sorted = ['size','text']
# sorted['size'] = bubble_size
# sorted['text'] = hover_text
# sizeref = 2.*max(data['size'])/(100**2)
#fig = px.line(data, x='Weight', y='MPG', title='')
fig = px.scatter(sorted, x='Weight', y='MPG', color='Manufacturer', size='Weight', size_max=30,
                 hover_name='Manufacturer')
fig.update_yaxes(dtick=10)
fig.update_layout(legend= {'itemsizing': 'trace'})
fig.show()

# dict for makers
# manuf = ['bmw', 'ford', 'honda', 'toyota', 'mercedes']
# manuf_data = {data.query("Manufacturer == '%s'" %Manufacturer)
#               for make in manuf}

print(data)
