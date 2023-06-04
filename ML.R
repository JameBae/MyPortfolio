library(tidyverse)
library(caret)
library(readxl)
library(randomForest)
library(MLmetrics)

df <- read_excel("House Price India.xlsx", sheet = 2)

df <- df %>%
  mutate(norprice = log(Price+1))

df <- df %>%
  rename("nbath" = "number of bathrooms",
         "nbed" = "number of bedrooms",
         "grade" = "grade of the house")

subdf <- df %>%
  select(norprice, nbath, nbed, grade)


# 1.split
set.seed(33)
n <- nrow(subdf)
id <- sample(1:n, size = 0.8*n)
train_data <- subdf[id, ]
test_data <- subdf[-id, ]

# 2.train
set.seed(33)
ctrl <- trainControl(method = "cv",
                     number = 5)

(lm_model <- train(norprice ~ .,
                  data = train_data,
                  method = "lm",
                  preProcess = c("center", "scale"),
                  trControl = ctrl))

(knn_model <- train(norprice ~ .,
                   data = train_data,
                   method = "knn",
                   preProcess = c("center", "scale"),
                   trControl = ctrl))

(randomForest_model <- train(norprice ~ .,
                   data = train_data,
                   method = "rf",
                   preProcess = c("center", "scale"),
                   trControl = ctrl))

# 3.score

p <- predict(lm_model, newdata = test_data)

# 4.evaluate

mae <- mean(abs(test_data$norprice - p))

# 5. save model

saveRDS(lm_model, "houseindia_lm.RDS")




