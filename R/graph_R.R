library(ggplot2)
library(tidyverse)
df = read.csv("cars-sample.csv")
ggplot()

df %>% ggplot() + geom_point(aes(x=Weight,y=MPG,color =Manufacturer,size = Weight),alpha = 0.5)
