import tweepy
import json

with open("credentials.json") as cred_file:
    credentials = json.load(cred_file)

auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)