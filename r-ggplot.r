
if (!require("knitr")) {
  install.packages("knitr") # do this once per lifetime
  require("knitr") # do this once per session
}
library("tidyverse")
library("tidyquant")
library("corrplot")
library("GGally")
library("ggplot2")
library("dplyr")

carsdf <- read.csv("C:/Users/apeco/Downloads/cars-sample.csv")
ggplot(carsdf, aes(x=Weight, y=MPG) ) + 
  geom_point( aes(x=Weight, y=MPG, color=Manufacturer, size=Weight, alpha= .5)) + 
  stat_ellipse(aes(color = Manufacturer), type = "t")
