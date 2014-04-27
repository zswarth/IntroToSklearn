import tweetpony

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

  def tweet_text(self, query):
    tweets = []
    a = self.api.search_tweets(q= query)
    b = a['statuses']
    for i in b:
      tweets.append(i['text'])
    return tweets

  @property
  def rate_limit_exceeded(self):
    return self.num_processed >= 175 


