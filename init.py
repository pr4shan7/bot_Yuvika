import tweepy
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# me = api.me()
p7 = 'pr4shan7'
p7_id = api.get_user(p7).id


def set_following():
    s = set()
    for friend in tweepy.Cursor(api.friends).items():
        s.add(friend.id)
    return s


following_list = set_following()


def set_toFollow():
    s = set()
    for follower in tweepy.Cursor(api.followers).items():
        s.add(follower.id)
    for follower in tweepy.Cursor(api.followers, p7).items():
        s.add(follower.id)
    s.remove(api.me().id)
    return s


follow_list = set_toFollow()


# rate_limit = api.rate_limit_status() 
