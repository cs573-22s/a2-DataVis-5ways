Assignment 2 - Data Visualization, 5 Ways  
===

# Excel

Link to the file: https://github.com/ColdCode0214/a2-DataVis-5ways/tree/main/Excel

Excel is an useful tool developed by Microsoft. 
It can help you to make the different tables and charts much easier, including pie chart, line chart, bar chart and so on.
You don't need to write code to generate the chart, just operating by using the graphical interface.
It's a much friendly tool for the people who are not familiar with coding.
However, it sometimes not as flexible as python or matlab. 
And if there are too much data, like over ten thousand, it sometimes difficult to see clearly in such a small chart.

Here is the chart with ordinary bubbles.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-Excel-1.png" width = "470" height = "400" alt="" align=center />

Here is the chart with 3D bubbles, which can make the bubbles more clear than the ordinary one.
And when you move your mouse above the bubble, you can see the detail value of it.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-Excel-2.png" width = "470" height = "400" alt="" align=center />


# Tableau

Link to the file: https://github.com/ColdCode0214/a2-DataVis-5ways/tree/main/Tableau

Tableau helps people see and understand data.
It is a powerful and fastest growing data visualization tool used in the Business Intelligence Industry.
Tableau combines data manipulation with beautiful charts. 
Its programs are so easy to use that companies can use it to drag and drop large amounts of data onto a digital "canvas" and create graphs in a blink of an eye. 
The idea of the software is that the easier the data on the interface is to manipulate, 
the better a company will be able to understand whether it's doing right or wrong in its area of business. 
It's also a much friendly tool for the people who are not familiar with coding.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-Tableau-1.png" width = "600" height = "370" alt="" align=center />

# Python

Link to the file: https://github.com/ColdCode0214/a2-DataVis-5ways/tree/main/Python

(To run this file, you need to put the data file "cars-sample.csv" in the same fold as this python file (A2-Python),
otherwise, it will fail and show the error as following)

<img src="https://github.com/ColdCode0214/pictures/blob/main/python-error.png" width = "870" height = "170" alt="" align=center />

Matplotlib is a Python 2D plotting library that produces publication-quality graphics in a variety of hardcopy formats and a cross-platform interactive environment. 
With Matplotlib, developers can generate plots, histograms, power spectra, bar graphs, error graphs, scatter plots, and more with just a few lines of code. 
For me, this Python method combined with Matplotlib is much easier compared with D3, 
since many functions are already implemented in the library and what we need to do is just call them and set the parameters.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-Python-1.png" width = "540" height = "500" alt="" align=center />

# R & ggplot2

Link to the file: https://github.com/ColdCode0214/a2-DataVis-5ways/tree/main/R

(If you want to run this file, you need to change the address of the data file. 
This is the local address of the data file on my pc and you need to change it in to the address of the file on your computer)

<img src="https://github.com/ColdCode0214/pictures/blob/main/r-code.png" width = "800" height = "250" alt="" align=center />


The ggplot2 package is the most exciting extension package for R graphics, and R is a language primarily focused on statistical computing.
It implements the "grammar of graphics", decomposes a plotting task into several subtasks, and the plotting can be completed as long as each subtask is completed. 
When making common graphics, only two steps are required: 
first, input the data displayed by the graphics into the ggplot() function, 
and then call a geom_xxx() function to specify the type of graphics, 
such as scatter plot, curve chart, box graphs, etc. 

Here is the chart with the ordinary requirement.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-R-1.png" width = "600" height = "400" alt="" align=center />

Here is the chart which use the other shapes to alternative the bubble in the previous one which can make the chart more clear and
more easy for people to distinguish different manufactor.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-R-2.png" width = "700" height = "400" alt="" align=center />

# D3

Link to the file: https://github.com/ColdCode0214/a2-DataVis-5ways/tree/main/D3

D3 is one of the most popular visualization libraries and is used by many other table plugins.
With D3, it will be more convenient for us to draw various graphics and coordinate axes.
It's quite flexible and we can add some interactive functions.

In my assignment, when you move your mouse on the bubble, the bubble will turn into red and become bigger. 
And when you move your mouse away, the bubble will return to the original color and size.
When you click on the bubble, it will move to the top of the chart.
This function is used to remove some unsignificant data, so that we can compare the other data more directly.
When you want the bubble which was moved to the top return back to the original position,
you can 'drag' it back to its position by keep your mouse press down and move your mouse down.
P.S. When you drag the bubble down, you should keep your mouse inside the bubble all the time, otherwise, the bubble will stop going down.
When you dragged the bubble back to the original position, you should first move your mouse outside of the bubble, then stop pressing down the mouse,
otherwise, the bubble will move to the top again.

<img src="https://github.com/ColdCode0214/a2-DataVis-5ways/blob/main/img/A2-D3-1.png" width = "719" height = "637" alt="" align=center />

# Technical Achievements
1.All of the charts are added grid.

2.All of the charts are added legends.

3.Added some additional functions on D3
- mouse move over a bubble: the bubble will turn into red and the size will become bigger.
  This function is used to make the select bubble more clear compared with other bubbles, 
  since some of the bubbles are overlapped together and hard to distinguish.
- mouse move away from one bubble: the bubble will return to the original color and size.
- click on the bubble: the bubble will move to the top of the chart
  This function is used to remove the unsignificant data, 
  inorder to make the significant data much easier to observe and compare.
- Press on the bubble which are removed on the previous step: the bubble can be dragged down to the original position
  But pay attention to the following things: 
  When you drag the bubble down, you should keep your mouse inside the bubble all the time, otherwise, the bubble will stop going down.
  When you dragged the bubble back to the original position, you should first move your mouse outside of the bubble, then stop pressing down the mouse,
  otherwise, the bubble will move to the top again.

# Design Achievements
- Most of the charts are added title.
- In the Excel chart, besides the ordinary bubble, I also use the 3D bubble instead of the ordinary bubble,
  which can make the chart more clear.
- In the R chart, besides the oridinary requirement, I also use other shapes instead of bubbles.
  Because some of the bubbles are overlapped together and are hard to distinguish.
- In the Tableau chart, I added the summary board which can show the maximum value, minimum value, average value and so on.

# Reference
- RGB color: https://www.sioe.cn/yingyong/yanse-rgb-16/
- How to use Python matplotlib: https://blog.csdn.net/gaotihong/article/details/80983937
- How to use R to draw a bubble chart: https://www.jianshu.com/p/55cb66acda6c
- D3 instruction: https://www.cnblogs.com/qiushichen/p/6104143.html
- R instruction: https://www.cnblogs.com/harywood/p/6993974.html
- How to add a legend for D3: https://blog.csdn.net/weixin_40444691/article/details/109469189
