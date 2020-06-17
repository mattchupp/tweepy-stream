import tweepy


# secrets
consumer_key = ''
consumer_secret = ''
access_token =''
access_token_secret = ''

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# post a tweet
# just here as a test
# ------
api.update_status('Hello from python!')


# Set up stream for tweets
class MyStreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print(status.text)

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener)

# Stream tweets about this topic
myStream.filter(track=['python'])
