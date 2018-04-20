#To extract Tweets from Twitter
#Developed By - Nimiya Joseph
#Date - 1-11-2018
#First we need to import all the libraries that we are going to use
import urllib3
import tweepy
import csv
import pandas as pd

#Twitter credentials
consumer_key = 'F0J7et4jBZFvT53h3PKWRkvRj'
consumer_secret = 'dJSxQ38z9HFZ4Uw9BE6Ym3rVg2s6PrSLsIXdSVYqechjq4gPg6'
access_token = '882593661896110081-8DEklfWjjp3RqYgLBp5N9Y6rCI9DrAc'
access_token_secret = '6hotP1UF1GtBLP1OjSy1SX49nmfUV0GJr0y4Asx5JLReU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#Create a CSV file to store the tweets scrapped
csvFile = open('twtrBigData.csv', 'a')

csvWriter = csv.writer(csvFile)

#The keyword used to extract tweets is BigData
for tweet in tweepy.Cursor(api.search,q="#BigData",count=100,lang="en",since="2017-10-24").items():
    csvWriter.writerow([tweet.text.encode('utf-8'), tweet.created_at])
