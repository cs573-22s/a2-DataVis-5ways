# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

Your goal is to use 5 different tools to make the following chart:

![ggplot2](img/ggplot2.png)

These features should be preserved as much as possible in your replication:

- Data positioning: it should be a downward-trending scatterplot as shown.  Weight should be on the x-axis and MPG on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at 10, 20, 30, etcetera.
- Color mapping to Manufacturer.
- Size mapping to Weight.
- Opacity of circles set to 0.5 or 50%.

Other features are not required. This includes:

- The background grid.
- The legends.

Note that some software packages will make it **impossible** to perfectly preserve the above requirements. 
Be sure to note where these do not support the features you need, but feel free to still use them.

You may write everything from scratch, or start with demo programs from books or the web. 
If you do start with code that you found, please identify the source of the code in your README and, most importantly, make non-trivial changes to the code to make it your own so you really learn what you're doing. 

Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project. 
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Each visualization should start with a top-level heading (e.g. `# d3`)
- Each visualization should include a screenshot. Put these in an `img` folder and link through the readme (markdown command: `![caption](img/<imgname>)`.
- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---

0. Your code should be forked from the GitHub repo.
1. Place available code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.
2. Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).

GitHub Details
---

- Fork the GitHub Repository. You now have a copy associated with your username.
- Make changes to fulfill the project requirements. 
- To submit, make a [Pull Request](https://help.github.com/articles/using-pull-requests/) on the original repository.

Grading
---

Grades on a 120 point scale. 
24 points will be based on your Technical and Design achievements, as explained in your readme. 

Make sure you include the files necessary to reproduce your plots.
You should structure these in folders if helpful.
We will choose some at random to run and test.

**NOTE: THE BELOW IS A SAMPLE ENTRY TO GET YOU STARTED ON YOUR README. YOU MAY DELETE THE ABOVE.**

# Python + Jupyter + Matplotlib + Seaborn

(Language)

Python is a high level general pupose language. It has many different packages for data visualization. Few of the popular ones are Matplotlib and Seaborn. Matplotlib allows making of almost all kinds of graphs with very basic graphics. Seaborn is built on top of Matplotlib and allows advanced graphics and better themes.

Jupyter is a web-based interactive environment for creating notebooks in Python. I have used Python inside a Jupyter notebook.

![matplotlib](img/Figure_Python.png)

Following are the steps that were followed: 
1. Import libraries like Pandas and Numpy to import and manipulate data. Matplotlib and Seaborn are visualization libraries which are also imported.
2. The csv was imported into the notebook as a pandas dataframe object.
3. A plot was created of the appropriate size. 
4. The grid in the background was matched just like in the provided chart. (ACH)
5. Parameters were passed into the scatterplot function which are explained as follows:
    - x : X variable
    - y : Y variable
    - hue: Color variable for the markers
    - Size: Size variable for the markers
    - Palette: Colors were passed to match the exact colors in the provided chart (ACH)
    - Alpha: Transparency (set to 0.4 instead of 0.5 to match provided chart)
    - Data: Source DataFrame
    - Size_norm: Domain of the size variable
    - Sizes: Range of the sizes on graph
    - Legend: Brief legend
6. The next function is to position the legend in the position in the provided chart (ACH)
7. The xticks and yticks were passed to mark the same ticks as in the provided chart (ACH)
8. The result was then displayed

Data Manipulation:
- As such no data manipulation was required.

Advantages: 
- Matplotlib and Seaborn allow us to craete visualizations in very few lines of code.

Disadvanatages: 
- Editing the legend is a little more complicated.

Future Scope:
- Although not a very high level of customization is possible, since data manipulation is really easy because of libraries like Pandas, this method will always remain popular.


# R + ggplot2

(Language)

R is a language and environment for statistical computing and graphics. ggplot2 one of the most popular and an open-source data visualization package for the statistical programming language R. Tidyverse is a collection of open source packages in R for tidy data.

![ggplot2](img/Figure_R.png)

Following are the steps that were followed: 
1. Import libraries ggplot2 and tidyverse.
2. The csv was imported into the script as a dataframe object.
3. A plot was initialized. 
4. ggplot2's geom_point() layer was used along with aesthetics functions to match the color and size.

Data Manipulation:
- No data manipulation was required.

Advantages:
- Minimal code
- The visualization matches the original chart exactly probably because the original chart was also created in R

Disadvantages:
- Takes time to find relevant documentation

Future Scope: 
- Since R allows a lot of other statistical analysis, R will always remain popular among data scientists. 

# Excel

(Tool)

Excel is a spreadsheet tool which features calculation capabilties along with graphing tools. It allows users to use many functions for data manipulation.

![excel](img/Figure_Excel.PNG)

Following are the steps that were followed: 
1. The csv was first converted into an excel format of xlsx because csv files although read into excel, do not allow graphing. 
2. The csv was imported into the script as a dataframe object.
3. Bubble chart was used to make the chart in excel.
4. For achieving the color scheme, the data had to be converted into a different format as shown:
![Excel data](Excel/excel_data.png)
5. Bubble plot function was then used with these different series being used as the values 
6. To match the color values, colors were selected manually for each series. 
7. The ticks were then edited. But not a very high level of customization was available there. Only the min and max values could be set, not the intervals between two ticks.
8. The legend worked for the colors, but there was again no option to edit legend to show the sizes of the circles.

Data Manipulation:
- Data had to be converted to allow the colors to be selected differently by manufacturer.

Advantages:
- No coding involved and is easy for people with all backgrounds.
- Once the data manipulation is done, colors can be manually selected for the different manufacturers.

Disadvantages:
- Selecting the data to plot on the chart was a little difficult
- Extra Data Manipulation is required
- Legends can not be edited to allow us to plot sizes 

Future Scope: 
- Even though Excel does not allow a very high level of customization, it is very simple to use and hence it will always remain a favourite.
- Power BI is already built on top of excel and allows more customization which might become the future.

# D3

(Language)

D3 is a javascript library for manipulating documents based on data. It helps create powerful visualizations.

![D3](img/Figure_d3.PNG)

Following are the steps that were followed: 
1. 2 svg elements were created, 1 for the graph and 1 for the legend.
2. Some values were initialized by creating arrays.
3. Function was created to build the scatter plot which included size and color variables as well. 
4. Then the axes were built in the function.
5. Legend was tried to be recreated in the position next to the graph as in the provided chart. It was found to be difficult.
6. The legend only contains the size variable and not the color variable.
 
Data Manipulation:
- No data manipulation was required.

Advantages:
- D3 allows more level of customization. 

Disadvantages:
- Difficult to debug the code
- It was difficult to position the legend next to the graph. 

Future Scope: 
- D3 allows us a very high level of customization and hence d3 has its advantages. But the user friendly nature of the other tools/languages may cause people to switch to the other tools instead. 

# Vegalite

(Language)

Data Manipulation:


Advantages:


Disadvantages:


Future Scope: 


## Technical Achievements


### Design Achievements

