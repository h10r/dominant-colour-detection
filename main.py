#!/opt/local/bin/python3.3

import os
import time
import pickle

import numpy as np
import mahotas as mh

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
	return clf.predict_proba( histogram )
	
def predict_from_filename( filename ):
	return predict_from_histogram( histogram_from_filename( filename ) )

if __name__ == "__main__":

	#while True:

	os.popen(CMD)
	
	time.sleep( 0.2 ) # average execution time: 0.141
	
	print( predict_from_filename(FILENAME) )

	time.sleep( 1 )


