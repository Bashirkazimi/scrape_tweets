# Scraping tweets containing a specific hashtag

This is a simple python program to scrape tweets that contains a specific hashtag. It uses Tweepy and can only retrieve tweets in the past 7 days. 

# Setup

- Clone the repo and install the requirements:

  `pip install -r requirements`

- Open a [Twitter Developer](https://developer.twitter.com) account and get the following credentials:
  - consumer key
  - consumer secret
  - access key
  - access secret
  
- Edit the `get_api()` function to fill in the credentials you just obtained from your Twitter Developer account

- Run the program to retrieve tweets.

- Example run to retrieve 1000 tweets published from October 15th until October 17th containing #someHashtag:

`python scrape_tweets.py someHashtag 2022-10-15 2022-10-17 1000`

- Note that the hashtag should be given without the prefix `#`, otherwise the program will ignore anything after it.
  
- It will run and save the tweets in a `csv` file in the current directory.




