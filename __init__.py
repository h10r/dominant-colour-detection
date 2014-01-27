#!/opt/local/bin/python3.3

import Histogram
import Classifier
import Test

if __name__ == "__main__":
    Test()

"""
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

	
#### MAIN ####



	

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
"""
