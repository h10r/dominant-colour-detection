#!/opt/local/bin/python3.3

import os
import sys
import re
import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt

import pickle
import code

import pylab as pl
from sklearn import linear_model, datasets
from sklearn.preprocessing import Imputer

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

	color_names = []

	X = []
	Y = []

	if dict_of_histograms:
		print("tonks: Loaded histograms")

		color_class_id = 0

		for key in dict_of_histograms.keys():			
			color_names.append( key )

			hists, bin_edges = dict_of_histograms[key]

			for hist in hists[:10]:
				X.append( hist )
				Y.append( [color_class_id] )
				
			color_class_id = color_class_id + 1

		iris = datasets.load_iris()
		Xiris = iris.data  # we only take the first two features.
		Yiris = iris.target

		X = np.array( np.asarray( X , dtype=np.float64 ) )
		Y = np.ravel( np.asarray( Y , dtype=np.float64 ) )

		"""
		imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

		X = imp.fit( X )
		X = imp.transform( X )
		
		Y = imp.fit( Y )
		Y = imp.transform( Y )
		"""

		print( X )
		print( Y )

		print( X.shape )
		print( Y.shape )

		print( "dataset.dtype")
		print( X.dtype )
		print( Y.dtype )

		print( "isfinite")
		print( np.all(np.isfinite( X )) )
		print( np.all(np.isfinite( Y )) )

		"""
		print( "X" )
		print( X )
		print( "Y" )
		print(  Y )

		return
		"""

		h = .02  # step size in the mesh

		logreg = linear_model.LogisticRegression(C=1e5)

		#code.interact(local=locals())

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

	else:
		print("tonks: ERROR: couldn't find histograms - Regenerate?")


if __name__ == "__main__":
	main()
	pass 

