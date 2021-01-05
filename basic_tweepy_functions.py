#!/usr/bin/env python3

import json

import tweepy

# Get tokens
with open("secrets/keys.json") as f:
    keys = json.load(f)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(keys["API"], keys["Secret"])
auth.set_access_token(keys["Access"], keys["Access Secret"])

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

### Verify credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

### Get the timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

### Make a tweet
api.update_status("Test tweet from Tweepy Python")

### Get user information
user = api.get_user("MikezGarcia")
print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

### Like some tweets
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

### Searching
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")


### Get trending topics
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])