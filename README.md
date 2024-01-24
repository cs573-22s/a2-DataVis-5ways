Assignment 2 - Data Visualization, 5 Ways  
---

Mingjie Zeng (671222265)   
Email:mzeng2@wpi.edu

In this assignment, I use Python+Matplotlib, D3, Flourish, R+ggplot, and Tableau way separately to achieve the visualization goal.


## Python + Matplotlib

Here is the file link:https://github.com/JasmineZZZ9/a2-DataVis-5ways/tree/main/Python%2BMatplotlib

Among the languages and tools used in this assignment, python and matplotlib are the combination I am most familiar with. I have used this to draw graphs before, but more for the purpose of enriching the presentation of the results rather than focusing on expressing the data itself. 

And in this assignment, it took some pains to get similar results to the example. I was impressed by a few points. One is that the result of the drawing is rather archaic and not very beautiful. In order to adjust it to be closer to the way ggplot presents it, many variables were adjusted, such as the color of the facecolor and the grid color and even the color of spines. This can cause new problems, for example, the priority of the grid adjusted to white has become higher, so it is presented above the scatter dots, so I need to find a way to solve the priority problem. Although none of this is a complex problem, there are many details that are troublesome. Another thing that impressed me was the legend problem. The model presented two different legends at the same time, and in the conventional way, the second initialized legend would overwrite the first one, which was a problem I had not encountered before, and there was a bit of tricky.

This is the scatter plot obtained in Python + Matplotlib way:

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/python%2Bmatplotlib.png" width = "600" height = "400" alt="" align=center />

The advantages of this approach are that first of all, python is a popular language, which is very versatile and easy to understand, and drawing in python is also very common and convenient. The disadvantage is that the drawing is more conventional, but there are many ready-made packages to make up for this.


## D3

Here is the file link:https://github.com/JasmineZZZ9/a2-DataVis-5ways/tree/main/d3

This part of work is based on a theme templates in D3.js Graph Gallery: https://www.d3-graph-gallery.com/graph/custom_theme.html in a mimicking ggplots style.
This is the results of d3 work: 

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/d3.jpg" width = "500" height = "600" alt="" align=center />

When exploring d3 there are a lot of excellent templates which is very happy, in fact, d3 is relatively simple to apply, but for people without html or css foundation, it will be a little difficult to accept. But because there are excellent examples, luckily I can learn a lot. One of the difficult parts for me in this section was to understand how d3 reads csv data and how it is used. Another novelty is how to bind the color with certain properties, I see a lot of methods, look forward to trying to achieve one by one later. In this part, my understanding of the html and svg is still not enough, for the canvas size is difficult to determine efficiently, the final rendering of the axis also has some strange. But d3 still plays an important role in interacting with the data in these tools, which makes me feel its simplicity and power.


## Flourish

Here is the file link:https://github.com/JasmineZZZ9/a2-DataVis-5ways/tree/main/Flourish

This is my first time using Flourish, an online platform that is very easy to use, very simple and clear for data manipulation, and the final result is perfect. Although the template provided by the online platform is not similar to the example, the information expressed is the same.
Here is the result:

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Flourish.png" width = "600" height = "400" alt="" align=center />


The platform is very comprehensive in its consideration of the various representations of data, with more than imaginable mapping forms, not just color, shape or size.

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Flourish-mapping.jpg" width = "450" height = "600" alt="" align=center />

What's more, this platform is very friendly for people who can't program, and the efficiency of making data visualization is also very high. You can just upload files to operate on the data directly, and the operation is also very straightforward and simple, which is easy to get started.

![image](https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Flourish-data.jpg)


## R + ggplot

Here is the file link:https://github.com/JasmineZZZ9/a2-DataVis-5ways/tree/main/R%2Bggplot

The combination of R and ggplot is very simple and efficient in use, and the presentation is really very smart and beautiful. It is really amazing that a very simple code can produce a very good effect. But the part I spent the longest time in this section is the deployment of the environment, because I have not touched R before, although his syntax is very straightforward and simple, but there are indeed many potholes when matching the environment, including the problem that ggplot somehow fail to generate images, and the problem that the compiler does not work. The process of rendering data with R is very cool, but it takes some hands-on time. Here is the final result rendered in R + ggplot：

![image](https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/R.png)

The effect looks very complicated but actually does not require people to do anything, the legend, color, even the size of the dots are automatically generated according to certain conditions. R can easily achieve effects that look fancy, such as gradient colors that meet certain conditions, including a well-matched and harmonious color style, different shapes, and different ways of filling, which will create a desire to explore.

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/R_color.png" width = "480" height = "400" alt="" align=left />
<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/R_color_2.png" width = "480" height = "400" alt="" align=right />




## Tableau

Here is the file link:https://github.com/JasmineZZZ9/a2-DataVis-5ways/tree/main/Tableau

Tableau is also a very convenient and smart platform, but compared to Flourish, I think it is slightly more complicated, but can do more things, such as some further manipulation of the data, summing and averaging, etc. Good effects can be fetched by using this platform:

<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Tableau.jpg" width = "600" height = "400" alt="" align=center />

Not only can Tableau directly exclude missing data, but you can also manipulate the presentation of data in detail from all angles:


<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Tableau-1.jpg" width = "280" height = "400" alt="" align=left />
<img src="https://github.com/JasmineZZZ9/a2-DataVis-5ways/blob/main/pics/Tableau-2.jpg" width = "280" height = "400" alt="" align=center />

Besides these basic ones, this platform has more professional ways to handle data. Next I will try to learn their mature ways to handle data and try to apply them to my own practice.


## Technical Achievements
- For myself, this is the first time I have tried using R and it's a very intereting. And for the two data visulization platform Fourish and Tableau, this is my first time to use them too, they bring me a lot surprise about visulization.
- Try a lot of different attributes about every function and methods to get the properiate format of data viz.
- The implement of two different lengends in python using add_artist() and patches is new and interesting to me.

## Design Achievements
- Some attempts were made in the R section to take advantage of its superiority to experience some beautiful designs, such as different shapes and fills, etc.
- Go to the color matching website specifically to select a more harmonious color to represent.
- Many attempts have been made for the beauty of the images, such as the placement and size of the legend, the ratio of the size of the dots and even the thickness of the grid, etc. have been adjusted accordingly.
