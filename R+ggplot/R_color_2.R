library(ggplot2)

data <- read.csv("cars-sample.csv", encoding = "UTF-8")

ggplot(data, aes(x = Weight, y = MPG, size = Weight, color = Manufacturer, shape = Origin)) + 
  geom_point(alpha = 0.5) +
  scale_color_brewer(palette = 'Accent') + scale_shape_manual(values = c(2,7,16))
  
