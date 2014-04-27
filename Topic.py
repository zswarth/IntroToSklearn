from twitter import Twitter
from cluster import KMeansClusterer
from cluster import SpectralClusteringCluster
from sklearn.cross_validation import cross_val_score
from collections import OrderedDict
from classify import PerceptronPredictor


class TopicAnalyzer(object):

	def __init__(self):
		self.twitter_api = Twitter()
		self.clusterer = SpectralClusteringCluster()

	def correlate(self, topic):
		a = ['Obama', 'Tea', 'Guitar']
		b = []
		for i in a:
			b.append(self.twitter_api.tweet_text_clean(i))
		c = []
		for i in b:
			c.extend(i)

		d = self.clusterer.cluster(c)
		total_error_rate = 0
		for idx, val in enumerate(d):
			difference = set(b[idx]) - set(d[idx])
			total_error_rate += len(difference)



		return total_error_rate


	def cross_validation(self):
		a = ['Obama', 'Tea', 'Guitar']
		b = []
		for i in a:
			b.append(self.twitter_api.tweet_text(i))
		c = []
		for i in b:
			c.extend(i)


		_ = self.clusterer.cluster(c)
		return cross_val_score(self.clusterer.clf, self.clusterer.X)


	def binary_topic(self, topic):
		all_tweets = OrderedDict()
		for i in self.twitter_api.tweet_text(topic, n_tweets = 100):
			all_tweets[i] = 1
		for i in self.twitter_api.tweet_text('Noise', n_tweets = 100):
			all_tweets[i] = 0

		some_tweets = OrderedDict()
		for i in self.twitter_api.tweet_text(topic, n_tweets = 10):
			some_tweets[i] = 1
		for i in self.twitter_api.tweet_text('Noise', n_tweets = 10):
			some_tweets[i] = 0

		return all_tweets, some_tweets
		
