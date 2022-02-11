import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("code/cars-sample.csv")

sb.set_style('darkgrid')
splot = sb.scatterplot(data=df, 
            x='Weight',
            y='MPG',
            hue='Manufacturer',
            size='Weight',
            alpha=0.5
            )

splot.set_xticks(range(2000,6000,1000))
splot.set_yticks(range(10,50,10))

plt.legend(fontsize='x-small', framealpha=0.8)

plt.show()

