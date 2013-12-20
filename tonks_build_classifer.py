#!/opt/local/bin/python3.3

import os
import glob
import sys
import re
import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt

import pickle
import code

import pylab as pl

from sklearn import linear_model


FILE_PATH = "../photos/hendrik"

HIST_BANDS = 128
ALPHA_BANDS = 0.1
SAVE_TO_FILE = True

h = .02

color_names = []

clf = linear_model.LogisticRegression(C=1e5)

print("tonks: Build classifier: STARTED")

#### CLASSES ####

class Histogram():

	def get_histogram_from_image( image_path ):
		img = mh.imread( image_path )

		hist, bin_edges = np.histogram( img, bins = range(HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		return hist

#### HELPER FUNCTIONS ####

def read_tonks_data_from_disk():
	try:
		return pickle.load(open("data/tonks.dat", "rb"))
	except:
		return False

def write_tonks_data_to_disk( tonks_data ):
	print("tonks: Save data to disk")
	pickle.dump( tonks_data, open("data/tonks.dat", "wb"))
	
#### MAIN ####

def plot_clf():
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

def direct_test():
	global color_names

	test_files = glob.glob( FILE_PATH + "/test/*" )

	print( test_files )

	for test_file in test_files:
		h = Histogram.get_histogram_from_image( test_file )
		clf_predict = clf.predict_proba( h )

		print("* " + test_file.split("/")[-1] )
		for p in clf_predict:
			for i in range(len(p)):
				if p[i] > 0.0:
					print( color_names[i] + "\t(" + str(p[i]) + ")" )
		print()

def main():
	global color_names

	dict_of_histograms = read_tonks_data_from_disk() # False

	X = []
	Y = []

	if dict_of_histograms:
		print("tonks: Loaded histograms")

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

		clf.fit( X, Y )

		direct_test()

	
	else:
		print("tonks: ERROR: couldn't find histograms - Regenerate?")


if __name__ == "__main__":
	main()
	pass 

