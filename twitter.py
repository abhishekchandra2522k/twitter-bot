from re import search
import tweepy
import time

auth = tweepy.OAuthHandler('','')

auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

search = 'python'
nrTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        # print('Tweet Liked')
        tweet.retweet()
        # print('Tweet Retweeted')
        time.sleep(516) # 216 sec because twitter has 50/3hr limit for RT and like
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break