import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_exchange_rate_etl():
    access_key = "${ACCESS_KEY}"
    access_secret = "${ACCESS_SECRET}"
    consumer_key = "${CONSUMER_KEY}"
    consumer_secret = "${CONSUMER_SECRET}"

    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)


    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@naira_rates', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    
    current_date = datetime.now()
    tweet_list = []

    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"run_time": current_date,
                        "user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv('exchange_rates_tweets.csv')
    # df.to_csv('s3://exchange-rates-airflow/exchange_rates_tweets.csv')

# run_exchange_rate_etl()