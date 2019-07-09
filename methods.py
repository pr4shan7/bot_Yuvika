from init import api, p7, tweepy


def follow_fs():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    print("Followed everyone following " + api.me().name)


def follow_p7fs():
    for follower in tweepy.Cursor(api.followers, p7).items():
        follower.follow()
    print("Followed everyone following " + p7)
