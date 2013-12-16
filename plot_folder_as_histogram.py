#!/opt/local/bin/python3.3

import os
import sys
import re

import numpy as np
import mahotas as mh

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print
print("plot_folder_as_histogram foldername")
print

def read_and_generate_histogram( a_file ):
	img = mh.imread( a_file )
	hist, bin_edges = np.histogram( img, bins=12 )

	return hist, bin_edges

def draw_histogram( x ):
	# the histogram of the data with histtype='step'
	n, bins, patches = plt.hist(x, 50, normed=True, histtype='step')
	plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

	# add a line showing the expected distribution
	#y = mlab.normpdf( bins, mu, sigma)
	#l = plt.plot(bins, y, 'k--', linewidth=1.5)

	#plt.plot(range(10), range(10))
	plt.title("Histogram")
	plt.show()

def read_each_file_in_folder( path ):
	print("Reading folder: " + path)
	
	x = []

	dirs = os.listdir( path )
	for a_file in dirs[0:5]:
		if a_file.endswith(".jpg"):
			hist, bin_edges = read_and_generate_histogram( path + a_file )
			x.append( hist )

	draw_histogram(x)

def main(folder):
	
	read_each_file_in_folder(folder)

if __name__ == "__main__":
		main(sys.argv[1])
