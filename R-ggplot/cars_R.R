#install.packages("ggplot2")
#install.packages("tidyverse")

library(tidyverse)
library (readxl)

cars <- read.csv("cars-sample.csv")


cars %>%
  filter(MPG <= 40) %>%
  ggplot (aes(x= Weight, y=MPG, colour = Manufacturer, size = Weight, alpha = I(0.5))) +
  geom_point()+
  labs (title = "Fuel Efficiency by Weight") +
  theme_minimal()
  
  ggsave("Cars_Rplot.jpg")