# -*- coding: utf-8 -*-
"""twitter_sentiment_analysis_rest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1APC-g8aSzpf_AcUIpDkLWKCRKBJ-CG9G
"""

url='http://50bbef5502be.ngrok.io/predict'

import json
import requests

request_data = json.dumps({'sentence':'bad performance by England'})

response = requests.post(url,request_data)

response.text

import tweepy

#my twitter key mvisanu10 mvisanu@gmail.com
consumer_key='<key>'
consumer_secret ='<secret>'
access_token = '<token>'
access_secret = '<acc secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,timeout=20)

tweet_text = 'vaccine';

tweets_list = []

for status in tweepy.Cursor(api.search,q=tweet_text,lang='en',result_type='recent').items(500):
        tweets_list.append(status.text)

len(tweets_list)

tweets_list[30]

import re

for i in range(len(tweets_list)):
  # get each tweet
  tweet = tweets_list[i]
  tweet = tweet.lower()
  # remove junk characters 
  tweet = re.sub(r'\W',' ',tweet)
  # remove one or more space
  tweet = re.sub(r'\s+',' ',tweet)
  # Remove all characters except a to z or A to Z and replace them with a space
  tweet = re.sub('[^a-zA-Z]',' ',tweet)
  # store the clean tweet back in the list
  tweets_list[i] = tweet

tweets_list[30]

positive_tweet = 0
negative_tweet = 0

for tweet in tweets_list:
  request_data = json.dumps({'sentence':tweet})
  response = requests.post(url,request_data)
  sentiment = response.text
  if sentiment == 'positive':
    positive_tweet += 1
  else:
    negative_tweet += 1

positive_tweet

negative_tweet

