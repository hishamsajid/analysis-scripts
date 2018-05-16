#3rd November, 2017

setwd("/Users/Hisham/Documents/slack_data analysis")
logs_csv <- read.csv("logs.csv")
View(logs_csv)
install.packages("binr")
logs_test <- logs_csv
library("binr")
time <- logs_csv$time
num_words <- logs_csv$num_words

logs_test$time <- as.POSIXct(as.numeric(logs_test$time), tz = 'GMT')

logs_test$time <- as.POSIXct(logs_test$time, origin="1970-01-01")

View(logs_test)
summary(logs_csv)

time <- logs_test$time
boxplot(time)
hist(time, density=100, prob=FALSE, breaks=12, col="lightblue")
#finding correlation between time and number of words
plot(time,num_words,main="words & time",pch=19, col="red", xlab = "Time", ylab = 'Number of words')
cor(time,num_words) #0.01090538 very little correlation between time and number of words
#however a positive relation has been established between the two variables
cov(time,num_words) 

binned_time <- binning(time)
binned_time <- binr::bins(time, target.bins = 24, minpts = 5)
binned_time$breaks <- bins.getvals(binned_time)


bins <- binned_time$binct

logs_test$time <- binned_time$binct


logs_test <- lapply(logs_test, cut, logs_test$time)
View(logs_test)

logs_test <- logs_csv
logs_test$time <- as.numeric(cut(logs_test$time, breaks = 24))

#View(binned_time$xtbl)

#binr::bins(time, target.bins = 24)


d_time <- density(logs_test$time)
plot(d_time, main = 'Time Density')
polygon(d_time, col = 'light blue')
title(main = 'Time Density')
View(d_time)
hour <- format(logs_test$time, "%H")
logs_test$hour <- hour
View(logs_test)

hist(main = 'Frequency Histogram',logs_test$time, density=100, prob=FALSE, breaks=24, col="lightblue",xlab = 'Time')


hist(main = 'Frequency Histogram',aslogs_test$hour, density=100, prob=FALSE, breaks=24, col="lightblue",xlab = 'Time')

hist(as.numeric(hour), density=100, prob=FALSE, breaks=24, col="lightblue")

View(time)