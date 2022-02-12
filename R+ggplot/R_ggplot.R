library(ggplot2)

data <- read.csv("cars-sample.csv", encoding = "UTF-8")

ggplot(data, aes(x = Weight, y = MPG, size = Weight, color = Manufacturer)) + 
  geom_point(alpha = 0.5)
