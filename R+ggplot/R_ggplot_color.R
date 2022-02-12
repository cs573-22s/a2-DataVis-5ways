library(ggplot2)

data <- read.csv("cars-sample.csv", encoding = "UTF-8")

ggplot(data, aes(x = Weight, y = MPG, size = Weight, color = MPG)) + 
  geom_point() +
  scale_color_gradient(low = "#227D51", high = "#A8D8B9")
