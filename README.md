# Twitter Bot for Me

Kinda want a twitter bot to handle being social and smart for me. So first I
want a program to look at csv (or something) to get the next tweet and then
tweet it out. Then I want a tweet manager to manage multiple twitter bots
handling different topics (like jokes, retweets, ML articles, etc.) and running
each program periodically based on a config. Then work on programs to create and
update those CSV daily.

So there are 3 sections; a twitter bot manager running twitter bots
periodically, actual twitter bot program to look at a csv and tweet something
out, and csv creators based on topics.

Looking majorly at this for direction: https://realpython.com/twitter-bot-python-tweepy/

# Design

## Twitter Bot

Main goal is to be generic enough to read any CSV and
just tweet stuff out and interact.

So the three actions I want it to take are as follows:

1. From last X number of tweets, choose one to retweet and repeat a few times a day.
2. Define Y <  2\*x, like a random number between 1 and Y/10 tweets
3. Text me a list of tweet for me to look at to see if I want to add a comment or not.
4. From a CSV file of tweet that I want to send out on a timer,
tweet out for me.

So there are a few functionalities this bot needs from twitter:

1. To read the last X number of tweets from my home
2. To like a tweet with it's id
3. To retweet a tweet with it's id
4. Get some basic stats about a tweet (likes, reposts, and who interacted with it)
5. Get information about users
6. Be able to follow a user with their id

There are also some other functionalities I would like it to have so I can do more analysis and interact with it more that does not involve the twitter api:

1. Talk to a database
2. Be able to text me securely
3. Allow each action to be run on it's own cron

## Twitter Bot Manager

Also fairly simple. Basically want to create a Daemon to run twitter bots
periodically based on a config file. The config file will basically be a list of
twitter bots with a cron schedule expression, the name of the twitter bot, and
link/something to point to the twitter bot to run.

Here are the steps for the program:
1. Load in config
2. Loop through configs for twitter bots to configure the cron
3. Sit back and relax

Thinking about using this: https://dev.to/damjand/python-scheduler-a-cron-job-replacement-54ep

# TODOS

- Run basic program
- Create basic functionality class
- Create database class to talk to my database
- Create python to run likes
- Create python to run retweets
- Create python to run CSV tweets
- Create python to send me links of interesting tweets to comment on
- Create manager to read in config and files to run on timers
