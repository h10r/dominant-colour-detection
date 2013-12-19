#!/opt/local/bin/python3.3

import os
import sys
import re
import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt
import pickle

import pylab as pl
from sklearn import linear_model, datasets

HIST_BANDS = 128
ALPHA_BANDS = 0.1
SAVE_TO_FILE = True

print("tonks: Build classifier: STARTED")

#### CLASSES ####

class ImageClassifier():

	def transform( self, image ):
		img = mh.imread( image )

		hist, bin_edges = np.histogram( image, bins = range(HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		return hist

	def predict(self, hist ):
		pred = self.clf.predict( hist )
		return {"scores" : pred}

#### HELPER FUNCTIONS ####


def read_tonks_data_from_disk():
	try:
		return pickle.load(open("tonks.dat", "rb"))
	except:
		return False

def write_tonks_data_to_disk( tonks_data ):
	print("tonks: Save data to disk")
	pickle.dump( tonks_data, open("tonks.dat", "wb"))
	
#### MAIN ####

def main():
	dict_of_histograms = read_tonks_data_from_disk() # False

	if dict_of_histograms:
		print("tonks: Loaded histograms")

		print( dict_of_histograms.keys() )
		print( len(dict_of_histograms) )

		iris = datasets.load_iris()
		X = iris.data[:, :2]  # we only take the first two features.
		Y = iris.target

		"""

		h = .02  # step size in the mesh

		logreg = linear_model.LogisticRegression(C=1e5)

		# we create an instance of Neighbours Classifier and fit the data.
		logreg.fit(X, Y)

		# Plot the decision boundary. For that, we will assign a color to each
		# point in the mesh [x_min, m_max]x[y_min, y_max].
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
		"""

	else:
		print("tonks: ERROR: couldn't find histograms - Regenerate?")


if __name__ == "__main__":
	main()
	pass 

