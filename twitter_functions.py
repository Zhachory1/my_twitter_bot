#!/usr/bin/env python3

import tweepy

class TwitterInterface:
    def __init__(self, consumer_key, consumer_secret, access_token):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        ### Verify credentials
        try:
            self.api.verify_credentials()
            print("Authentication OK")
            self.authenticated = True
        except:
            print("Error during authentication")
            self.authenticated = False

    def check_auth(self):
        if not self.authenticated:
            print("Error during authentication, please use the correct tokens to access twitter.")

    def get_last_X_tweets(self, last_X):
        pass

    def like_tweet(self, tweet_id):
        pass

    def retweet(self, tweet_id):
        pass

    def get_tweet_stats(self, tweet_id):
        pass

    def get_user_stats(self, user_id):
        pass

    def follwer_user(self, user_id):
        pass