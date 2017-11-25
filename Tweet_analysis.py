#Use this python script to generate tweets from Twitter. 
#Use for tweet sentiment analysis
import tweepy
import csv
import pandas as pd
####input your credentials here. 
####You will need to register on Twitter to get the credetials under Twitter Developer.(https://apps.twitter.com)
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('AFINN-111.csv', 'a')#http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#ANTIFA",count=100,#Use any search term you'd like
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
#
