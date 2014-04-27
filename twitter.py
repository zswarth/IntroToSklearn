import tweetpony
import re

class Twitter(object):

  access_token = '2376312126-YUCVGSOYgP9kQJNx46AOwIRCVddKUPpcf7fDkJH'
  access_token_secret = '8ugXhMtCYq0IHP5KAzM16xoiMvXkXIpWtTWvk52V9QCbS'
  consumer_key = '7gNH5uIskTOTACpCOKgbw'
  consumer_secret = '4wiDP0muI5Krudzt8cVT30w1QKqMKjqjLGYTobbKY'

  def __init__(self):
    self.reset_auth_token()
    self.try_later = []
    self.num_processed = 0

  def reset_auth_token(self):
    self.api = tweetpony.API(
        consumer_secret = self.__class__.consumer_secret,
        consumer_key = self.__class__.consumer_key,
        access_token = self.__class__.access_token,
        access_token_secret = self.__class__.access_token_secret
    )


  def tweet_text(self, query, n_tweets = 5):
    tweets = []
    a = self.api.search_tweets(q= query, count = n_tweets)
    b = a['statuses']
    for i in b:
      tweets.append(i['text'])
    return tweets

  


  def post_status(self, text):
    user = self.api.user
    try:
      self.api.update_status(status = text)
    except tweetpony.APIError as err:
      print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
    else:
      print "Yay! Your tweet has been sent!"


  @property
  def rate_limit_exceeded(self):
    return self.num_processed >= 175 





class TestTwo(object):

  access_token = '2376312126-yMSAYDhxUhiNM7eN5G4AtNpzckYdHluIsE4MFoB'
  access_token_secret = 'tVbz1bF4AHNqvLKqEu49IjSxKNSXUT075xNptb86nEpTw'
  consumer_key = 'rbJIP2DBQ8dlPCYUoR7aw'
  consumer_secret = 'gNFBcPzpN9SWDKZtoLV9ZjC173qJB642fPEVBeBQ'

  def __init__(self):
    self.reset_auth_token()
    self.try_later = []
    self.num_processed = 0

  def reset_auth_token(self):
    self.api = tweetpony.API(
        consumer_secret = self.__class__.consumer_secret,
        consumer_key = self.__class__.consumer_key,
        access_token = self.__class__.access_token,
        access_token_secret = self.__class__.access_token_secret
    )

  def tweet_text(self, query, number):
    tweets = []
    tags = []
    a = self.api.search_tweets(q= query, count = number)
    b = a['statuses']
    for i in b:
      tweets.append(i['text'])
      tags.append(i['text'])
    return tweets, tags


  def my_tweets(self, user):
    tweets = []
    a = self.api.user_timeline(screen_name = user)
    for i in a:
      tweets.append(i['text'])
    return tweets

  def post_status(self, text):
    user = self.api.user
    try:
      self.api.update_status(status = text)
    except tweetpony.APIError as err:
      print "Oops, something went wrong! Twitter returned error #%i and said: %s" % (err.code, err.description)
    else:
      print "Yay! Your tweet has been sent!"




  @property
  def rate_limit_exceeded(self):
    return self.num_processed >= 175 
