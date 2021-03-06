import tweepy.auth
import tweepy
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status("This tweet was made in python!")
