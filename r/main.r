library("tidyverse")

data <- read.csv("C:/Users/Jasper/Documents/Classes/CS573 Data Visualization/a2-DataVis-5ways/cars-sample.csv")

ggplot(data, aes(x=Weight, y=MPG)) + 
  geom_point(aes(x=Weight, y=MPG, color=Manufacturer, size=Weight, alpha=0.5))
