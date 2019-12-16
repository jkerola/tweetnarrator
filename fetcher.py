#!usr/bin/python3
import tweepy
import json


def authenticate(fileName):
    "Load credentials for twitter authentication."
    with open(fileName) as cred_file:
        credentials = json.load(cred_file)
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])
    api = tweepy.API(auth)
    return api

def getTweets(api):
    "Fetch tweets based on keyword"
    public_tweets = api.home_timeline(count = 4)
    filtered_tweets = []
    for tweet in public_tweets:
        print(tweet.text)
        #filtered_tweets.append({tweet.user: tweet.text})

        
    return filtered_tweets

credentials = "credentials.json"


if __name__ == "__main__":
    api = authenticate(credentials)
    getTweets(api)
