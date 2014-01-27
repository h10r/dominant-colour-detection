#!/opt/local/bin/python3.3

import os
import glob
import sys
import re

from operator import itemgetter

import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt

import pickle
import code

import pylab as pl

from sklearn import linear_model

FILE_PATH = "../photos/hendrik"

ALPHA_BANDS = 0.1

GENERATE_FILES = True

SAVE_TO_FILE = True

h = .02

color_names = []

clf = linear_model.LogisticRegression(C=1e5)
	
#### MAIN ####


def direct_test():
	global color_names

	test_files = glob.glob( FILE_PATH + "/test/*" )

	for test_file in test_files:
		h = Histogram.get_histogram_from_image( test_file )
		
		clf_predict = clf.predict_proba( h )

		unsorted_predictions = []

		print("* " + test_file.split("/")[-1] )
		for p in clf_predict:
			for i in range(len(p)):
				if p[i] > 0.0:
					unsorted_predictions.append( [color_names[i], p[i] ] )
		
		sorted_predictions = sorted( unsorted_predictions, key=itemgetter(1), reverse=True)

		for res in sorted_predictions[:3]:
			color, percentage = res
			print( color + "\t" + str(int(100*percentage)).zfill(2) + "%" )
		print()

def generate_and_return_classifier():
	dict_of_histograms = load_histograms_from_disk() # False

	X = []
	Y = []

	if dict_of_histograms:
		print("Loaded histograms")

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

		return clf
	return False
	

def main():
	global color_names

	if GENERATE_FILES:
		clf = generate_and_return_classifier()
		write_classifier_to_disk( clf )
	else:
		clf = load_classifier_from_disk()
	
	if clf:
		direct_test()
	else:
		print("ERROR: couldn't find classifier")

if __name__ == "__main__":
	main()
	pass 
