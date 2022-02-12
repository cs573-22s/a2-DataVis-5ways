# 02-DataVis-5ways
James Plante
jplante@wpi.edu

# p5.js
Processing is a software library that is used for drawing and teaching new programmers how to code. It has a number of implementations such as versions targeted at Java, JavaScript, and Python. I used the p5.js library for this project due to difficulties getting a Processing-like library working in Python 3 (the official version uses Jython as its runtime so it is still targeting Python 2.7). It also has an integrated editor/sketchbook that allows code to be easily shared online.

![p5js](img/p5js.png)

While the web editor was very easy to use and edit in (save for a lack of a Vim mode), the process of creating a scatter plot/bubble chart was very time consuming since there were no built-in libraries to do this, meaning some manual work had to be done in terms of data processing. While importing the data is relatively easy with the `loadStrings` function, most of the CSV parsing had to be done by hand which was made easier using higher order functions such as `Array.map()` to parse the lines one by one and do the necessary data conversions, which largely consisted of doing a group by operation using a dictionary by category to separate out the manufacturer time series. 

The plotting of the bubbles was relatively easy since Processing has a built in way to convert ranges of values to locations on the canvas (the function is coincidentally named `map()`). The main issue with plotting presented itself when having to figure out how to manually draw the grid lines and making sure that they were in scale with the data. The title, axis, and tick labels had to be drawn manually also using text drawing primitives, which was somewhat tedious compared to other libraries where this is already done. To get the y axis title in the correct orientation I had to learn how to to a transformation
to rotate the canvas in the right orientation to draw the text. Drawing the legend was a largely manual
process by careful positioning of text, ellipse, and rectangle primitives (with loops of course). I also added some interactivity as an extra, so you can mouse over the bubbles and get data associated with these points.

While I found this exercise in creating a bubble chart in p5 to be educational, I would not recommend this tool since it takes much more effort to make a simple bubble chart than other libraries and interactivity is much harder since rendered objects do not have any internal state or event handling, making interactivity somewhat difficult for more advanced tasks.

# R + ggplot2 + R Markdown
R is a commonly used programming language for visualization, ggplot2 being a popular library for R. I primarily based my code on the lecture notes, so it uses the geom_point() layer. Overall, it was very easy to use and had no issues with creating this bubble chart to the exact specifications (the whole visualization code is 3 lines of code).

![ggplot2](img/ggplot2.png)

# Matplotlib
Matplotlib is a Python library that is used for plotting and making charts similar to MATLAB's plotting libraries that are included in the language. The data processing for this library was involved was not trivial: I still had to do grouping on the data using a dictionary to plot the individual categories and do manual CSV parsing. However it was relatively easy to do the actual plottting of the graph: it was mostly just calling functions to set axis titles, specifying that a legend needed to be created, and plotting each category. The only difficulty that I had in this section was that I had to manually determine the size of each bubble which I scaled based on the range of all of the weights. I would recommend this tool since it does not require a lot of effort, the syntax is easy to follow, and it still gives control to the user if they need to.

![matplotlib](img/matplotlib.png)

# Excel
![excel](img/excel.png)

Excel is a Microsoft spreadsheet application that has a graphical way of plotting data and doing data visualization. I surpingly had a more difficult time with this application than with other graphical data visualization tools. For one, while Excel has native support for bubble charts, it did not detect that the Manufacturers were categories. My solution to this was to filter the orginal CSV by category, paste the result into a new Sheet per category, then plot them as individual series, which seemed to fix the issue. I also had to manually scale the bubble sizes since they did not have a sane default scale: this was surpisingly difficult to do due to my lack of experience with Excel, but managed to make the chart work in the end. I would recommend this tool to someone who does not want to learn how to code or they have very basic data visualization needs since for more complex tasks, it is easier just to code it.

# d3
![d3](img/d3.png)

d3 is a powerful JavaScript library that allows for interactive and appealing visualizations. I found using d3 relatively easy to use due to prior experience, although I found it difficult to debug with due to the nature of how it will silently fail. In terms of data processing, I was pleasantly suprised I did not have to do grouping of individual time series. I also found it easier to add new geometry in since it has a relatively intuitive syntax once you get past the initial learning curve. While it is a powerful tool, I would mainly use it if I needed to do a very advanced visualization with a lot of interactive elements.

# Flourish
![flourish](img/flourish.png)

Flourish is a graphical visualization tool that exposes a lot of options to the user and does automatic data processing. This was a very easy application to use: creating the chart took less than 15 minutes. It already had a bubble chart template so I used it, uploaded the CSV, set the correct axes, enabled a legend, set the opacity and grid lines, and I was done. One aspect that I did not appreciate was the lack of customization so I was not able to find an option right away to include the size of the Weights as an option. Also I was not able to set a custom scaling for the size of the bubbles so it uses just a linear scale. I would see this tool being useful for simple visualizations, although I would not use it for more advanced visualizations due to the lack of control you have over the final image.

## Technical Achievements
- **Interactivity in p5.js**: I enabled some interactivity in the p5.js sketch, whenever you hover your mouse over a data point, it will show the other attributes of the data point.
- **Creating a legend in d3 and p5.js**: I attempted to create similar legends to the ggplot plot which was generally non-trivial. For d3 I learned how to create a legend by following a tutorial (link in the source code) and in p5, I did it manually.
- **Used Greater than Five Tools**: I used 6 tools in total for this project, 4 of which were code-based

### Design Achievements
