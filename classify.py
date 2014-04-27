cfrom sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import Perceptron



class BinaryPredictor(object):

	def __init__(self, training, test):
		self.clf = None
		self.cv = None
		self.X, self.Y = self.pre_process(training)
		self.test_X, self.test_Y = self.pre_process(test)

	def pre_process(self, text):
		if not self.cv:
			self.cv = CountVectorizer()
			self.cv.fit(text.keys())
		X = self.cv.transform(text.keys())
		Y = text.values()
		return X,Y

	def train(self):
		self.clf.fit(self.X, self.Y)

	def predict(self, text):
		feature, nothing = self.pre_process({t:0 for t in text})
		return map(bool, self.clf.predict(feature))

	def evaluate(self):
		return cross_val_score(self.clf, self.X, self.Y)

class PerceptronPredictor(BinaryPredictor):

	def __init__(self, training, test):
		super(PerceptronPredictor, self).__init__(training, test)
		self.clf = Perceptron(shuffle = True)




tweets = {
	"This is a tweet" : 0,
	"This is a tweet about climbing": 1
}