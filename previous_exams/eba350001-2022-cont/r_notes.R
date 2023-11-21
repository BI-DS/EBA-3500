data <- read.csv("exams.csv")

lm(math.score ~ ., data = data)