import pickle
import pylab as pl

import numpy as np    

from sklearn import linear_model

class Classifier():

	def __init__(self, histogram):
		self.clf = linear_model.LogisticRegression(C=1e5)

		self.histogram = histogram

		histograms_from_disk = self.histogram.load_from_disk()

		self.X = []
		self.Y = []

		self.color_names = []

		if histograms_from_disk:
			self.X,self.Y = self.generate( histograms_from_disk )

			self.clf.fit( self.X,self.Y )
		else:
			print("Error while initializing Classifier")
			return False

	def generate(self, dict_of_histograms):
		color_class_id = 0

		for key in dict_of_histograms.keys():			
			color_names.append( key )

			hists, bin_edges = dict_of_histograms[key]

			for hist in hists:
				
				if not np.all( np.isfinite( hist ) ):
					pass
				else:
					X.append( hist )
					Y.append( [color_class_id] )
				
			color_class_id = color_class_id + 1

		X = np.asarray( X , dtype=np.float64 )
		Y = np.asarray( Y , dtype=np.float64 )

		Y = np.ravel( Y )

		return X,Y

	def colorname_by_index( self, index ):
		return self.color_names[ index ]

	def predict_from_histogram(self, histogram):
		return self.clf.predict_proba( histogram )
	
	def predict_from_filename(self, filename):
		return self.predict_from_histogram( self.histogram.from_filename( filename ) )

	def plot():
		x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
		y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
		xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
		Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

		# Put the result into a color plot
		Z = Z.reshape(xx.shape)
		pl.figure(1, figsize=(4, 3))
		pl.pcolormesh(xx, yy, Z, cmap=pl.cm.Paired)

		# Plot also the training points
		pl.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=pl.cm.Paired)
		pl.xlabel('Sepal length')
		pl.ylabel('Sepal width')

		pl.xlim(xx.min(), xx.max())
		pl.ylim(yy.min(), yy.max())
		pl.xticks(())
		pl.yticks(())

		pl.show()
