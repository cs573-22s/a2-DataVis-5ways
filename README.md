# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===
## 1) Javascript + D3
![a2-D3](https://github.com/johvanniperez/a2-DataVis-5ways/blob/a2-johvanniperez-Johvanni-Perez/D3Graph.PNG)
Out of all the libraries I used to recreate the cars sample dataset graph, I felt that D3 gave me the most control in creating a custom graph/visual. However, I did find that it was the trickiest to place and emphasize certain chart elements and aesthetics. For example, I found a "tick" functionality in the D3 library that would allow a programmer to specify the number of axes tick marks could be displayed in the graph. Unfortuanley, this tick functionality did not allow me to specify how the units or intervals are incremented on the graph (i.e the model graph provided shows that the MPG units increments from 10 to 20 to 30...). 

## 2) Python + Matplotlib
![a2-python](https://github.com/johvanniperez/a2-DataVis-5ways/blob/a2-johvanniperez-Johvanni-Perez/a2-python/a2-python-graph.png)
Matplotlib is an easy library to use and implement and recreating the graph using this library and python was not as difficult as I thought. The only challenge in recreating the model graph was specifying the weight for the sizing of the data points. For example, I did some arithmetic transformation on the dataset to manually specify the weight that would be applied to each individual data point. While I was able to chang the sizing for each data point, it is not as accurate as the one shown in the model graph. I ended up playing with different weight values to see what looked best/worse. One other thing with noting is that matplotlib does not support multiple legends being displayed on a singular graph.

## 3) R + ggplot2
![a2-RStudio](https://github.com/johvanniperez/a2-DataVis-5ways/blob/a2-johvanniperez-Johvanni-Perez/a2-RStudio/a2-RStudio/a2-RStudioggplot.png)
In comparison to the other libraries, ggplot2 was the easiest and most efficient of them all. I was able to recreate the model graph using just this library in RStudio and with only 3 lines of code or so.

## 4) PowerBI
![a2-PowerBI](https://github.com/johvanniperez/a2-DataVis-5ways/blob/a2-johvanniperez-Johvanni-Perez/a2PB/PowerBIGraph.PNG)
I have used PowerBI before to create data visualizations before and it is a relatively easy tool to use. However, it was quite tricky when it came to trying to recreate the graph. For example, before I could even graph the data, I had to transform the dataset so that the null values would be removed in order for the data type to be correctly identified for colulmns Weight and MPG. With null values the data gets read as "text" type, but without it is read as "numeric" type and without it being identified as of "numeric" type, PowerBI does not graph the data how one would expect. Like matplotlib, PowerBI does not allow multiple legends to be displayed.

## 3) Excel
![a2-Excel](https://github.com/johvanniperez/a2-DataVis-5ways/blob/a2-johvanniperez-Johvanni-Perez/a2Excel/ExcelGraph.png)
Like PowerBI, I have used Excel to create visualizations and the toolsets it provides for making these visuals. Excel wasn't too tedious, but it did have some shortcomings. For example, in order to create a color coded scatter plot where each color represented a manufacturer in the dataset, I had to first sort and order the dataset by manufacturers. For each manufacturer, I had to manually insert the respective data into the graph. After doing so, I then had to repeatedly change the formatting of the data such as the transparancy of the data points for each manfucturer group. Like PowerBI and matplotlib, Excel does not support multiple legends on a particular graph.

## Technical Achievements
- Matplotlib was tricky enough in trying to get one legend for the Manufacturer/colors. I was able to implement this legend using Line2D
- Applying weight to the data points for four different ways as they did not handle it as easy as ggplot2
- Mapping color to Manufacturer

### Design Achievements
- Using different colors to identify the manufacturers
- Demonstrating the axes and their labels
