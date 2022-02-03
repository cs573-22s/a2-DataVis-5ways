import plotly.express as px
import pandas as pandas

# Limitation of library
# Cannot support multiple legends

data = pandas.read_csv("cars-sample.csv")

# colorscheme based on d3 categorical swatches
colorscheme = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
               "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]

manufacturers = data['Manufacturer'].unique().tolist()
manufacturers.sort()
colors = {manufacturer: colorscheme[idx]
         for idx, manufacturer in enumerate(manufacturers)}

scatter = px.scatter(data, x="Weight", y="MPG", size="Weight", color="Manufacturer", color_discrete_map=colors, hover_name="Car", size_max=20, opacity=0.5)

scatter.show()
