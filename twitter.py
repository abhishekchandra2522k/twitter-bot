from re import search
import tweepy
import time

auth = tweepy.OAuthHandler('aySso9HxjmV5dVkw6H2FGKss4','86vTao2HM9zAI9dAYSL7zOW0cv36VkQgk6AEIFHHdVitNJADRc')

auth.set_access_token('1272433034159992833-Bq4MDAFktLN7PxEH6iKkzIPgdcK7KW', 'YiUgFbFn6yJDkLdQqrpq9uOqVTrbWOVoB9VvjWgSmR6Ir')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

search = 'javascript'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        print('Tweet Liked')
        tweet.retweet()
        print('Tweet Retweeted')
        time.sleep(216) # 216 sec because twitter has 50/3hr limit for RT and like
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break