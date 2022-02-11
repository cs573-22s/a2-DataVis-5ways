
# R + ggplot2 + R Markdown

For the first recreation of the scatterplot I used R. Specifically, I made use of the geom_point function within the ggplot2 library.
Building the plot in this fashion was honestly very quick after I dug through the documentation a bit and allowed for easy manipulation of the data and resulting visualization.

Firstly, you can see my best attempt at recreating this graph. You'll note that it is nearly identical.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/r%20plot.png)

Next, I decided to iterate on the design. Quite honestly, I found it unnecessary to make any drastic changes to any of the visualization. Changing font sizes or colors felt like they would simply be changes just for the sake of it and not to improve the overall delivery of the information presented. I did however, decide to implement a color palette from the R package Viridis to make the plot color blind friendly, which felt like a simple yet meaningful improvement to the visualization.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/r%20plot%202.png)

Finally, to touch on a quick technical and design note, I also made use of the facet_wrap function in ggplot2, to visualize each of the manufacturer subsets individually. It makes use of a deeper functionality of the package while also parsing the data for easier processing by the user.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/rplot3.png)



# D3

For the next recreation of the plot I made use of d3. To create this plot I made use of multiple different methods and shapes within d3. To keep things breif, I first created the svg that houses the plot, I set a light grey rectangle as the background of the plotting area, I manually created and postioned both size and color legends, and then I loaded in the data and actually began generating the plot. Below you'll find a list of tutorials I utilzed and amalgamed together to create this plot.

So first you can see my best attempt at recreating this plot, which seems pretty spot on aside from legend positioning and colors.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Screen%20Shot%202022-02-11%20at%202.38.23%20PM.png)

Then you can see my redesign which makes the plot more accessible to colorblind individuals through the use of a colorblind friendly palette. Additionally, I've made some technical achievement by making this iteration interactable. As you can see, mousing over a specific dot highlights all other dots of that manufacturer and greys out the others.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Screen%20Shot%202022-02-11%20at%202.38.31%20PM.png)
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Screen%20Shot%202022-02-11%20at%202.38.38%20PM.png)

https://ghenshaw-work.medium.com/customizing-axes-in-d3-js-99d58863738b
https://bl.ocks.org/wadefagen/ce5d308d8080130de10f21254273e30c
https://www.d3-graph-gallery.com/graph/scatter_grouped.html
https://www.d3-graph-gallery.com/scatter.html
https://www.d3-graph-gallery.com/graph/scatter_grouped_highlight.html

# Excel

Then I attempted to recreate the plot through the use of Microsoft Excel. This method was noticably harder than methods like R or python, which was honestly unexpected. What I noticed is that this tool is useful for beginners, but if you have any specific needs or design visions for your visualization you are better off generating it using a programming language like R or Python.

Following the trend, you can first see my recreation of the plot. You'll note the axes are slightly different, the colors differ, and that the size legend was generated maually. These facts are due to the limitation of the program.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Screen%20Shot%202022-02-11%20at%202.33.36%20PM.png)

Then, I again redeisgned with the purpose of making the plot color vlind accessible.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Screen%20Shot%202022-02-11%20at%202.33.47%20PM.png)


# Python

For my 4th method, I created the plot using python and the packages: Seaborn & matplotlib. Both packages are made specifically for data visualization within a python environment. In terms of use I would measure this approach on the same level as R. Essentially, it proved to have the most customization and ease of use, while also providing the lowest barrier to entry. 

So first, for my recreation you can see that below, and while colors and the amount of increments on the size legend differ the plot is virtually the same.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/seaborn%20plot%201.png)

Then similar to past methods, I focused my design efforts on making the plot color blind friendly through the use of a specific color palette and unqiue symbols for each manufacturer.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/seaborn%20plot%202.png)


# Flourish

Finally for my last method I used the online tool flourish. This was my first interaction with the tool and it was honestly very positive. It provides a very low barrier to entry in terms of data visualization (potentially the lowest of all 5 methods used). The potential of this platform is quite large and for those with no programming experience I would really recommend this more than excel. However, what it provides in breadth, it lacks in depth of customization, which is why you'll note the legend placement and lack of the size legend overall is present in my creations.

So for the first creation, you'll note in essence this graph is the same despite differeing colors.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Data%20Viz%20A2.png)

For design, you can see the use of a color blind friendly palette. Of note floursih provides very easy access to the creation of interactive visualizations, however to export them as an html file for that to be maintained requires a subscription. So I intened for an interactive legend similar to the functionality in my d3 iteration, however I did not want to give them my credit card-- so imagine it.
![this is an image](https://github.com/njtourtillott/a2-DataVis-5ways/blob/main/img/Data%20Viz%20A2-2.png)



## Technical Achievements
- Created an interactive visualization using d3, which allowed the user to highlight and mouse over specific manufacturers.
- made use of the facet wrap command in ggplot2 to create an easier to digest visualiztion for unique manufacturer trends (half a design acheivement too).

### Design Achievements
- rather than reinvent the wheel, I opted to make all the visualizations more accessible to a colorblind friendly audience. This felt more effective than nitpicking an already effective visualization.
