import tweepy
from tweepy import OAuthHandler
import ConfigParser
import json
import urllib3 
from tweepy import Stream
import feed_analyzer
import gif_creater
import argparse
from tweepy.streaming import StreamListener
from random import randint

consumer_key = 'oschi9olfj4EqJordQhLYkNGs'
consumer_secret = 'Cs8DaQUMLLH79J6szXsHAH3ueXgIS5QJrOqM7p2UYroWlBdtTC'
access_token = '967502485840568321-YTgmhJWKDWYCFEfcKCPU5EuBp6cpIVO'
access_secret = 'ldZaiZd45wJVJqBIUVIAGZfkKecmR4bDDkf5toxCaUQbt'

def ConfigSectionMap(section):
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def argument_parser(parser):
    parser.add_argument('-t', '--hashtag', type=str, help='Enter a hashtag to attack')
    parser.add_argument('-u', '--username', type=str, help='Enter a username to attack')
    parser.add_argument('-n', '--numtweets', type=int, help='Enter the number of tweets to attack', default=1)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    argument_parser(parser)
    args = parser.parse_args()
    htag = args.hashtag
    uname = args.username
    urllib3.disable_warnings()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twit = tweepy.API(auth)
    # Get a tweet, process it, create a gif, tweet a reply
    # if the tweet is an RT, get the next tweet, and repeat the step above
    # Repeat the above steps until the req num of tweets are posted
    with open('feed.json', 'w')as out:
        count = 0
        tweet_num = 0
        while count < args.numtweets:
            tweet_num +=1
            if htag is not None:
                status = tweepy.Cursor(twit.search, q='#'+htag, rpp=100, tweet_mode="extended").items(tweet_num)
            elif uname is not None:
                status = tweepy.Cursor(twit.user_timeline, screen_name='@'+uname, tweet_mode="extended").items(tweet_num)
            else:
                print('No inputs: Attacking News Feed')
                status = twit.home_timeline(screen_name = 'wandering_raps',count=1, tweet_mode="extended")
            for tweet in status:
                if (tweet.retweeted) or ('RT @' in tweet.full_text):
                    continue
                tweet_text = tweet.full_text
                word_list = feed_analyzer.tweet_analyze(tweet_text) 
                print word_list
                gif_creater.create_gif(word_list)
                status_msg = "Haha"
                if len(word_list) < 1:
                    continue  
                filename = 'myfile%d.gif'%(randint(1,2))
                print tweet.__dict__['id']
                screen_name =  tweet.__dict__['user'].__dict__['screen_name']
                try:
                    pic = twit.media_upload(filename)
                    twit.update_status(status_msg+" @"+screen_name, tweet.__dict__['id'], media_ids = [pic.media_id_string])
                    count +=1
                except:
                    print ("Error uploading gif, Trying the next tweet")
                    continue 
