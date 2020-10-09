#!/usr/bin/env python3

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("jKdVeYOyRXRdCrm1k3kQI0Zs1",
    "Uzqt2KX2buarRLcdTbqsEn2SVTg5vKNpZYzfqkKrViTs93G713")
auth.set_access_token("1314374192620621825-M3lYxPOKKzHhKlqpoiJpnc1yOMM72t",
    "mbH58BPJSGvOZLrTti3gdFbuq5CSnu1nDucABzsGf31M1")

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