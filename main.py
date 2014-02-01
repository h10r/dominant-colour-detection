#!/opt/local/bin/python3.3

import os
import time
import pickle

import numpy as np
import mahotas as mh

from operator import itemgetter

from sklearn.linear_model import LogisticRegression

HIST_BANDS = 4096

clf, _, _, color_names = pickle.load(open("data/cached_classifier.bin", "rb"))

FILENAME = "/tmp/current_screenshot.png"
CMD='screencapture -x -o ' + FILENAME

def colorname_by_index( index ):
	return color_names[ index ]

def histogram_from_filename( filename ):
	img = mh.imread( filename )

	hist, bin_edges = np.histogram( img, bins = range(HIST_BANDS), normed=True)
	hist = hist.clip(0.0,0.1)

	return hist

def predict_from_histogram( histogram ):
	clf_predict = clf.predict_proba( histogram )

	unsorted_predictions = []

	for p in clf_predict:
		for i in range(len(p)):
			if p[i] > 0.0:
				unsorted_predictions.append( [color_names[i], p[i] ] )

	sorted_predictions = sorted( unsorted_predictions, key=itemgetter(1), reverse=True)

	for res in sorted_predictions: #[:3]:
		color, percentage = res
		print( color + "\t" + str(int(100*percentage)).zfill(2) + "%" )
	print()

def predict_from_filename( filename ):
	predict_from_histogram( histogram_from_filename( filename ) )

if __name__ == "__main__":

	#while True:

	os.popen(CMD)
	
	time.sleep( 0.2 ) # average execution time: 0.141
	
	predict_from_filename(FILENAME)

	#time.sleep( 1 )
