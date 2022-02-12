# https://stackoverflow.com/questions/60962274/plotly-how-to-change-the-colorscheme-of-a-plotly-express-scatterplot
# https://plotly.com/python/plotly-express/
# https://plotly.com/python/figure-labels/
# https://plotly.com/python/tick-formatting/#using-tickformat-attribute

#dir(px.colors.qualitative)

import pandas as pd
import plotly.express as px

file = pd.read_csv("cars-sample.csv")

img = px.scatter(
    file, 
    x =  'Weight', 
    y = 'MPG', 
    color = 'Manufacturer', 
    color_discrete_sequence = px.colors.qualitative.Bold,
    size = 'Weight', 
    size_max = 20
) 

img.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=20,
        color="Brown"
    ),
    xaxis = dict(
        tick0 = 2000,
        dtick = 1000
    ),
    yaxis = dict(
        tick0 = 10,
        dtick = 10
    )
)
img.show()
