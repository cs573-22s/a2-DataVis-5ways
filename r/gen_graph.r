
install.packages('ggplot2')
library(ggplot2)

data <- read.csv("C:\\Users\\truma\\Documents\\DataVis\\a2-DataVis-5ways\\cars-sample.csv", header=TRUE, sep=",")
print(data)
wt <- data$Weight
mpg <- data$MPG
manu <- data$Manufacturer
p <- ggplot()
p <- p + geom_point(data=data, aes(wt, mpg, alpha=0.5, size=wt, color=manu)) + scale_size_continuous(name="Weight", range=c(1, 10))
p
#  xlab="Weight", alpha=0.5, col=factor(manu) ,ylab="MPG", pch=19)
methods(plot)
