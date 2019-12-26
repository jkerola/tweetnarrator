#!usr/bin/python3
from time import sleep
import tweepy
import re
import json
import pyttsx3

credentials = "credentials.json"
keyword = "Guilty Gear"
subsequent_pass = 0

def authenticate(fileName):
    "Load credentials for twitter authentication."
    with open(fileName) as cred_file:
        credentials = json.load(cred_file)
    cred_file.close()
    auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
    auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])
    api = tweepy.API(auth)
    return api

def getTweets(api, keyword):
    "Fetch tweets based on keyword"
    filtered_tweets = []
    for tweet in api.search(q=keyword, lang="en", count=2, tweet_mode="extended"):
        text = filterText(tweet.full_text)
        author = tweet.author.name
        # using , to create pauses without TTS reading slash n
        text = "From " + author + ", " + text + ", "
        filtered_tweets.append(text)
    return filtered_tweets

def filterText(text):
    "filters out links, usernames etc from tweets"
    ## thank you SO
    text = re.sub(r'http\S+', '', text)
    text = re.sub("\\n", ", ", text)
    text = re.sub("@\S+", "", text)
    return text

def speak():
    "Reads fetched tweets out loud."
    engine = pyttsx3.init()
    with open("tweets.json") as tweets_file:
        tweets = json.load(tweets_file)
    tweets_file.close()
    for line in tweets:
        engine.say(line)
        print(line)
        engine.runAndWait()
    engine.stop()
    return 1

def saveTweets(tweets):
    "Saves fetched tweets locally"
    with open("tweets.json", "w") as tweets_file:
        json.dump(tweets, tweets_file)
        tweets_file.close()

def compareLastTweets(new_tweets):
    "Compares whether new tweets have been made since last time."
    with open("tweets.json") as tweets_file:
        last_tweets = json.load(tweets_file)
    tweets_file.close()
    if new_tweets == last_tweets:
        return 1
    else:
        return 0

def main():
    "Main function that loops"
    tweets = getTweets(api, keyword)
    if subsequent_pass:
        while compareLastTweets(tweets):
            print("sleeping until new tweets appear...")
            sleep(30)
    saveTweets(tweets)
    if speak():
        return 1
    else:
        return 0


if __name__ == "__main__":
    api = authenticate(credentials)
    while main():
        subsequent_pass = 1
        continue