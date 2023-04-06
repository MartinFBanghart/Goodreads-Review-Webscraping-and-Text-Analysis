# Goodreads-Review-Webscraping-and-Text-Analysis

This project takes webscraped data from https://www.goodreads.com/ to create a dataset for the purpose of building a spam review filtering model and analytical visualizations in a graph database.

The dataset stems from the Top 100 books picked by Times magazine on goodreads.com (https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels).

The scraper is built within python utilizing the libraries Selenium and BeautifulSoup. After retrieval, all data is saved and loaded into flat files and preprocessed. Transformations are then applied to vectorize the review text data for implementation within ML models to identify spam reviews. After determining a sufficient model, flagged reviews are cleaned from the final dataset and pushed for uploading into the database.

The database of choice for graphical representation of the data is Arango.

