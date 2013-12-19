#!/opt/local/bin/python3.3

import os
import sys
import re
import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt
import pickle

HIST_BANDS = 128
ALPHA_BANDS = 0.1
SAVE_TO_FILE = True

print("tonks: Build classifier: STARTED")

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
		# print( dict_of_histograms )
	else:
		print("tonks: ERROR: couldn't find histograms - Regenerate?")


if __name__ == "__main__":
	main()

