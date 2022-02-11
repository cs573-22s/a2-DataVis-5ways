# 02-DataVis-5ways
The following is Assignment 2 for CS573.

# Tableau
Tableau is a data visualization tool that allows users to easily create visualizations using imported data. Using the desktop version I was able to create the scatterplot.

In order to view each individual point I ensured the values were not aggregated measures. I then dragged Weight to the columns and MPG to rows. In order to have the graph colored based on Manufacturer, I dragged it to the color mark and set the opacity to 50%. I adjusted the size of the points to be based on the Weight by dragging Weight into the size mark. Both of these actions added a Legend to the right of the graph. In order to get the proper axis labels, I edited the axis to not include 0, which allowed it to start at the proper values. 

I have a fair amount of Tableau experience so this was fairly simple for me. Hovering over each point will allow the user to see more information about which manufacturer it is, the mpg and the weight of it. 


![tableau](img\TableauGraph.JPG)

# R + ggplot2 + R Markdown

R is a programming language used for statistical computing and graphics, so it is very useful in creating a scatterplot. I used RStudio for it. I used the package ggplot2, in conjunction with the tidyverse package to allow for the data visualization. 

Using 'ggplot()', made it very simple to plot the graph by indicating the x and y values. I also used 'geom_point()' to edit the aesthetics of the graph, adding color and changing the size of the points. 


![ggplot2](img\RGraph.JPG)

# Flourish
Flourish is an increasingly popular data visualization tool that is very intuitive to learn and use to create great visualizations. These graphics can be created in stories or exported to images or embedded in websites. 

It was very simple to upload the necessary data to the website and select the data needed for the x and y values, as well as the color and size selection. This was the simplest tool used to create the graph. Their color scheme is great as well, with visually pleasing color choices that can be easily distinguished


![flourish](img\Flourish Graph.png)

# Python
Python can also be used to create a scatter plot. In my example I used 'pandas', a software library written for data manipulation, to read the csv file. I also used 'matplotlib.pyplot', which is a collection of functions that operate like matlab, to help with graphing. I used the 'scatter()' function to graph the data, indicating the x and y axis, transparency and size. The dataset was small enough that using 'scatter()' over 'plot()' did not affect the efficiency of the code. I had to divide the size by 25 to get the circles to be smaller and easier to distinguish. I was also able to label the graph. 

I ran into difficulty trying to color the circles, because matplotlib.pyplot requires color names in order to use the 'color='. I created a dictionary of what color should correspond to each manufacturer. Using that, I had it assign the color of each dot. 


![Python](img\PythonGraph.JPG)

# d3
d3 is a JavaScript library used for visualizing data using web standards. I used an svg to graph the scatter plot. It was able to read the csv file and assign the x and y values to variables. After it read the file, it used a function to build the scatterplot and also had a tester function to ensure the data was loaded properly by pasting to the console. I used the example provided on the website to guide me through building out this plot.

The 'd3.scaleLinear()' function was used to construct a linear relationship for the x and y axis. The color was also assigned to be based on the manufacturer. Then the size of each dot had to be set based on the weight. Then the svg was built with the dots based on their corresponding size. There were also x and y axis constructed to be used in the function to label the graph. 

This was the most difficult of the five ways to construct the graph. There are many little components that need to be completed in order for the graph to be created. For a while, I could not get the graph to load until I reconstructed how the function was called so that the data could be read and type casted before it was being used in future code. I also had difficulty getting the size of the dots to correspond to the weight. I was also unable to build out the legends on the side of the graph. 

gh-pages url: https://evbruk.github.io/a2-DataVis-5ways/


![d3](img\d3Graph.JPG)


## Technical Achievements
- **Python**: Adding in a color to manufacturer dictionary in the Python graph to allow for each manufacturer to have a specific color.

## Design Achievements
- **Tableau**: In the Tableau graph, I set up each dot so that the user could hover over and see what its specific detail was. 
- **d3**: For the d3 graph, the pre-designed schemeCategory10 was used to color the points.
- **Easy to Understand Deisgn**: Each graph was easy to read and understand. The sizing of the dots in the Python graph were made smaller so that they were more legible. 

