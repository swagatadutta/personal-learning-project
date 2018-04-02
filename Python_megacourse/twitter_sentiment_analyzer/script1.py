import tweepy
from textblob import TextBlob

consumer_key = "dcBBbMQ8gJpWTu2GUr0sVAl08"
consumer_secret = "XmbX5gQLk2kGBKInTIpuHqpwLpvunMuHoSwDxbAtvJiHg7JdnD"

access_token = "978983350416240641-XgBhqkgSWHWpqFzRwnCNqwFYmM08aaa"
access_token_secret = "6ALx3VkPlXNaMhsjO7E21q7WenOrt2uhyrWTH529k0jmx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search("Gun")

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
