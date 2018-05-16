#3rd November, 2017

setwd("/Users/Hisham/Documents/slack_data analysis")
logs_csv <- read.csv("logs_enhanced.csv",fileEncoding = "latin1")
#encoding changed to latin1 to avoid getting a multibyte string error
logs_test <- logs_csv

library(tm)
library(RTextTools)
install.packages("tm")
install.packages("slam")

install.packages('RTextTools',dependencies = TRUE)

message_utf8 <- iconv(message,"latin1" ,"UTF-8","")
View(message_utf8)
logs_test$snippet = 'NO'
testSampple = "```"
if(substr(message_utf8,0,3) == testSampple) {
  logs_test$snippet = 'YES'
}


View(logs_test)
logs_test$code <- 'NO'

logs_test$message_utf8 <- message_utf8

logs_test$code[substr(logs_test$message_utf8,0,3) == testSampple &
                 substr(lo)] <- 'YES' 

testSnippet = '`'
logs_test$snippet <- 'NO'
logs_test$snippet[substr(logs_test$message_utf8,0,1) == testSnippet & 
                  substr(logs_test$message_utf8,1,2) != testSnippet] <- 'YES' 


substr(message_utf8,0,3)

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

#binned_time <- binning(time)
#binned_time <- binr::bins(time, target.bins = 24, minpts = 5)
#binned_time$breaks <- bins.getvals(binned_time)


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

write.csv(logs_test,file = 'logs_enhanced.csv',fileEncoding = 'UTF-8')

csv2 <- read.csv('logs_enhanced.csv')
View(csv2)
message <- logs_test$message
View(message)




View(logs_csv)

hist(main = 'Frequency Histogram',logs_test$time, density=100, prob=FALSE, breaks=24, col="lightblue",xlab = 'Time')


hist(main = 'frequent.csvency Histogram',aslogs_test$hour, density=100, prob=FALSE, breaks=24, col="lightblue",xlab = 'Time')

hist(as.numeric(hour), density=100, prob=FALSE, breaks=24, col="lightblue")

View(time)
