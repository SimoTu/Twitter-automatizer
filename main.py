import config
import tweepy
import random

try:
    file = open('twitter.txt', 'r')
    array = []
    for x in file:
        text = x.rstrip()
        array.append(text)
except:
    print("An exception occurred")

selected = random.choice(array)
print("Selected tweet: " + selected)

client = tweepy.Client(
    bearer_token=config.BEARER_TOKEN,
    consumer_key=config.API_KEY,
    consumer_secret=config.API_KEY_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET)


response = client.create_tweet(text=selected)
print(response)
