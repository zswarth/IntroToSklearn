from twitter_with_re import Twitter
from sklearn.cross_validation import cross_val_score
from collections import OrderedDict
from classify import PerceptronPredictor

class TopicAnalyzer(object):

	def __init__(self):
		self.twitter_api = Twitter()

	def binary_topic(self, topic, n_tweets = 100):
		all_tweets = OrderedDict()
		for i in self.twitter_api.tweet_text(topic, n_tweets = n_tweets):
			all_tweets[i] = 1
		for i in self.twitter_api.tweet_text('Noise', n_tweets = n_tweets):
			all_tweets[i] = 0

		some_tweets = OrderedDict()
		for i in self.twitter_api.tweet_text(topic, n_tweets = 10):
			some_tweets[i] = 1
		for i in self.twitter_api.tweet_text('Noise', n_tweets = 10):
			some_tweets[i] = 0

		return PerceptronPredictor(all_tweets, some_tweets)

	def classification_scores(self, topic, n_tweets = 100):
		predictor = self.binary_topic(topic, n_tweets)
		return predictor.evaluate()