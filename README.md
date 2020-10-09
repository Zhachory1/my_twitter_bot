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

Super simple pipeline. Main goal is to be generic enough to read any CSV and
just tweet stuff out.

Here are the steps for the program:

1) Read in CSV
2) Choose a tweet
3) Read in Auth from external variables
4) Construct a twitter request and send
5) Log and store tweet response in database

## Twitter Bot Manager

Also fairly simple. Basically want to create a Daemon to run twitter bots
periodically based on a config file. The config file will basically be a list of
twitter bots with a cron schedule expression, the name of the twitter bot, and
link/something to point to the twitter bot to run.

Here are the steps for the program:
1) Load in config
2) Loop through configs for twitter bots to configure the cron
3) Sit back and relax

Thinking about using this: https://dev.to/damjand/python-scheduler-a-cron-job-replacement-54ep

## Tweet Maker
TODO