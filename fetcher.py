#!usr/bin/python3
import tweepy
import re
import json
import pyttsx3

credentials = "credentials.json"
keyword = "Guilty Gear"

def authenticate(fileName):
    "Load credentials for twitter authentication."
    with open(fileName) as cred_file:
        credentials = json.load(cred_file)
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])
    api = tweepy.API(auth)
    return api

def getTweets(api, keyword):
    "Fetch tweets based on keyword"
    filtered_tweets = []
    for tweet in api.search(q=keyword, lang="en", rpp=5):
        text = filterText(tweet.text)
        print(text)
        filtered_tweets.append(text)
    return filtered_tweets

def filterText(text):
    "filters out links from tweets"
    ## thank you SO
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\\n', ",", text)
    text = re.sub(r'\b@\S', "", text)
    return text

def speak(text):
    "Speaks given text out loud."
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def saveTweets(tweets):
    with open("tweets.json", "w") as tweets_file:
        json.dump(tweets, tweets_file)

if __name__ == "__main__":
    api = authenticate(credentials)
    tweets = getTweets(api, keyword)
    speak(tweets)
    saveTweets(tweets)