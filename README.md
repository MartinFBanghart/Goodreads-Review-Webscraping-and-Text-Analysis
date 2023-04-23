# Goodreads-Review-Webscraping-and-Text-Analysis

This project takes webscraped data from https://www.goodreads.com/ to create a dataset for the purpose of exploring the relationship between book ratings by reviewers and their reviews.

The dataset stems from the Top 100 books selected by Times magazine on goodreads.com (https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels).

The scraper is built within python utilizing the libraries Beautiful and Selenium. After retrieval, data is preprocessed and transformed for suitable for suitable loading into Arango (GraphDB). 

In order to accurately examine the relationship between reviews and ratings, a Spam detector is developed using NLP and Machine Learning Techniques to indentify and filter out irrelevant reviews, whose presence in the dataset may affect the accuracy of our results. Once these irrelevant reviews are filtered, exploratory analysis is performed using AQL to query the database and statistical tests to assess the significance our results.

