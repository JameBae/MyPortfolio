library(tidyverse)
library(rvest)

imdb <- "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"

movie_name <- imdb %>%
  read_html() %>%
  html_elements("h3.lister-item-header") %>%
  html_text2()

ratings <- imdb %>%
  read_html() %>%
  html_elements("div.ratings-imdb-rating") %>%
  html_text2() %>%
  as.numeric()

genre <- imdb %>%
  read_html() %>%
  html_elements("span.genre") %>%
  html_text2()

df_imdb <- data.frame(movie_name, ratings, genre)

View(df_imdb)

======================================

comspec <- "https://benchmarks.ul.com/compare/best-cpus?amount=0&sortBy=POPULARITY&reverseOrder=true&types=MOBILE,DESKTOP&minRating=0"

cpu <- comspec %>%
  read_html() %>%
  html_elements("a.OneLinkNoTx") %>%
  html_text2()

price <- comspec %>%
  read_html() %>%
  html_elements("td.list-tiny-none") %>%
  html_text2()

scores <- comspec %>%
  read_html() %>%
  html_elements("span.bar-score") %>%
  html_text2() %>%
  as.numeric()

df_score <- data.frame(scores)

df_score <- df_score %>%
  select(scores) %>%
  filter(scores < 10 )

df_cpu <- data.frame(cpu, price, df_score)

View(df_cpu)
  
