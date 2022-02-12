library(ggplot2)
library(tidyverse)

carsdf <- read.csv("~/GitHub/a2-DataVis-5ways/cars-sample.csv")

carsdf %>% ggplot() + 
  geom_point( aes(x=Weight, y=MPG, color=Manufacturer, size=Weight, shape=Origin), alpha=0.5 )
