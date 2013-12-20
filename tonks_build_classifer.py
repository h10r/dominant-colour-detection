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

from sklearn import neighbors

HIST_BANDS = 128
ALPHA_BANDS = 0.1
SAVE_TO_FILE = True

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

		X = np.asarray( X , dtype=np.float64 )
		Y = np.asarray( Y , dtype=np.float64 )

		Y = np.ravel( Y )

		knn = neighbors.KNeighborsClassifier(n_neighbors=2)
		print(knn)

		knn.fit( X, Y )

		test_files = glob.glob('data/test/*.jpg')
		print( test_files )

		print( color_names )

		for test_file in test_files:
			h = Histogram.get_histogram_from_image( test_file )
			

			colour_match = int( knn.predict( h )[0] )		
			print( color_names[colour_match] + " for : " + test_file )
	

	else:
		print("tonks: ERROR: couldn't find histograms - Regenerate?")


if __name__ == "__main__":
	main()
	pass 

