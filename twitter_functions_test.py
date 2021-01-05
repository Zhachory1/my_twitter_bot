import unittest
import json
import pprint
from twitter_functions import TwitterInterface

# Not really testing anything, really. Since the data coming
# back might be different, since we are attaching to an API,
# we can't really guarantee consistency.

# So I am using this just to make sure the API works by testing
# all my functions, and not checking the output.

# Really the functionality will be similar to basic_tweepy_functions,
# but this has structure around it.

# Big thing here is that I want to test without changing the environment.
# So all the likes and retweets I will clean up at the end of the test.

class TestTwitterInterface(unittest.TestCase):
    def setUp(self):
        with open("secrets/keys.json") as f:
            keys = json.load(f)
            self.api = TwitterInterface(keys["API"], keys["Secret"], keys["Access"], keys["Access Secret"])

    def test_get_user(self):
        pprint.pprint(self.api.get_user("MikezGarcia"))
        self.assertTrue(True)

    def test_get_trends(self):
        pprint.pprint(self.api.get_trends())
        self.assertTrue(True)

    def test_search(self):
        pprint.pprint(self.api.search("Python"))
        self.assertTrue(True)

    def test_get_tweets_from_home(self):
        pprint.pprint(self.api.get_tweets_from_home(3))
        self.assertTrue(True)

    def test_like_tweet(self):
        pprint.pprint(self.api.like_tweet(20)._json)
        self.api.tweepy_api.destroy_favorite(20)
        self.assertTrue(True)

    def test_retweet(self):
        pprint.pprint(self.api.retweet(20)._json)
        self.api.tweepy_api.unretweet(20)
        self.assertTrue(True)

    def test_get_tweet_stats(self):
        pprint.pprint(self.api.get_tweet_stats(20))
        self.assertTrue(True)

    def test_follow_user(self):
        pprint.pprint(self.api.follow_user("zhachory1")._json)
        self.api.tweepy_api.destroy_friendship("zhachory1")
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()