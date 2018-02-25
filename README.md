# gif-tweet

Requirements:

python-2.7
tweepy
giphy-python

How to Run:

fill 'twitter customer_key', 'costumer_security', 'access_token', 'access_token_security' fields in twitter_feeder.py

execute ./twitter_feeder.py <options> to run the script

What it does?

Reads a tweet, creates a funny gif response for the tweet, and post the gif as a reply.

Options:

-t <trendname> to read a tweet from the trend [optional]  

-u <username> to read a tweet from a specific username [optional]

-n <tweet_num> to read 'tweet_num' non repititive, non-reposted, original tweets from above two feeds, default = 1

Otherwise reads a tweet from the news feed and creates a funny gif tweet as a reply


