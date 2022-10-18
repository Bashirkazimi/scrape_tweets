import pandas as pd
import tweepy
import time

import datetime
import sys


# Code copied and adapted from: https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/

def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Location:{ith_tweet[2]}")
        print(f"Following Count:{ith_tweet[3]}")
        print(f"Follower Count:{ith_tweet[4]}")
        print(f"Likes:{ith_tweet[5]}")
        print(f"Retweet Count:{ith_tweet[6]}")
        print(f"Tweet Text:{ith_tweet[7]}")
        print(f"Hashtags Used:{ith_tweet[8]}")


# function to perform data extraction
def scrape(words, date_since, numtweet, filename, api, date_until):

        # Creating DataFrame using pandas
        db = pd.DataFrame(columns=['username',
                                   'description',
                                   'location',
                                   'following',
                                   'followers',
                                   'likes',
                                   'retweetcount',
                                   'text',
                                   'hashtags'])

        # We are using .Cursor() to search
        # through twitter for the required tweets.
        # The number of tweets can be
        # restricted using .items(number of tweets)
        tweets = tweepy.Cursor(api.search_tweets,
                               words,
                               since_id=date_since,until=date_until,
                               tweet_mode='extended').items(numtweet)


        # .Cursor() returns an iterable object. Each item in
        # the iterator has various attributes
        # that you can access to
        # get information about each tweet
        list_tweets = [tweet for tweet in tweets]

        # Counter to maintain Tweet Count
        i = 1

        # we will iterate over each tweet in the
        # list for extracting information about each tweet
        for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                location = tweet.user.location
                following = tweet.user.friends_count
                followers = tweet.user.followers_count
                likes = tweet.favorite_count
                retweetcount = tweet.retweet_count
                hashtags = tweet.entities['hashtags']

                # Retweets can be distinguished by
                # a retweeted_status attribute,
                # in case it is an invalid reference,
                # except block will be executed
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])

                # Here we are appending all the
                # extracted information in the DataFrame
                ith_tweet = [username, description,
                             location, following,
                             followers, likes,
                             retweetcount, text, hashtext]
                db.loc[len(db)] = ith_tweet

                # Function call to print tweet data on screen
                printtweetdata(i, ith_tweet)
                i = i+1
        

        # we will save our database as a CSV file.
        db.to_csv(filename)



def get_api():
    # Enter your own credentials obtained from twitter developer account
    consumer_key = "xxxx"
    consumer_secret = "xxxxx"
    access_key = "yyyyy"
    access_secret = "yyyyy"
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
   
    return tweepy.API(auth, wait_on_rate_limit=True)



if __name__ == '__main__':
    start_time = time.time()
    hashtag = sys.argv[1]
    date_since = sys.argv[2]
    date_until = sys.argv[3]
    numtweet = sys.argv[4]
    print('Scraping {} tweets for {} from {} until {}'.format(numtweet, hashtag, date_since, date_until))
    api = get_api()   
    filename = 'tweets_from_{}_until_{}.csv'.format(date_since, date_until)
    scrape(words, date_since, numtweet, filename, api, date_until)
    total_time = time.time() - start_time
    print('Scraping has completed! Total time: {} seconds'.format(str(datetime.timedelta(seconds=int(total_time)))))

