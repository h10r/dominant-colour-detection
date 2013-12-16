#!/opt/local/bin/python3.3

import os
import sys
import re

import numpy as np
import mahotas as mh

from matplotlib import pylab as plt

BINS = 16

# @TODO: Make sure the graph is cleared after each folder

def read_file_and_return_histogram( a_file ):
	img = mh.imread( a_file )
	
	return np.histogram( img, bins=BINS, normed=True )

def draw_histogram( histograms_in_folder, label ):
	print(label)

	for histogram in histograms_in_folder:
		bins, edges = histogram
		left,right = edges[:-1],edges[1:]

		X = np.array([left,right]).T.flatten()
		Y = np.array([bins,bins]).T.flatten()

		plt.plot(X,Y)
		plt.show()

def draw_histogram_inception( x, label, DEBUG=False ):
	# the histogram of the data with histtype='step'

	n, bins, patches = plt.hist( x, BINS, histtype='step' )
	print("*"*20)
	print(n)
	print(bins)
	print(patches)
	print(patches[0])
	print("*"*20)

	#plt.setp( patches, 'facecolor', 'g', 'alpha', 0.75 )

	# add a line showing the expected distribution
	#y = mlab.normpdf( bins, mu, sigma)
	#l = plt.plot(bins, y, 'k--', linewidth=1.5)

	#plt.plot(range(10), range(10))
	plt.title("Histogram")
	
	if DEBUG:
		plt.show()

	plt.savefig("plots/" + label + ".png")

def read_each_file_in_folder( path ):
	print("plot_folder_as_histogram: Reading folder: " + path)

	label = path.split("/")[-2]

	parent_folder = os.listdir( path )

	for dir_item_and_label in parent_folder[0:2]:
		full_path = path + "/" + dir_item_and_label

		# for all directories in path
		if os.path.isdir( full_path ):
			# print("is path " + full_path + " - label: " + dir_item_and_label)

			dirs = os.listdir( full_path )

			histograms_in_folder = []

			# for file in sub directory
			for file_in_dir in dirs[0:5]: # @TODO remove the 6 file limit!
				if file_in_dir.endswith(".jpg"):
					try:
						histograms_in_folder.append( read_file_and_return_histogram( full_path + "/" + file_in_dir ) )
					except Exception:
						print("plot_folder_as_histogram: ERROR reading " + full_path + "/" + file_in_dir)

			print("plot_folder_as_histogram: STATS: " + dir_item_and_label + ": " + str(len( histograms_in_folder )))

			draw_histogram( histograms_in_folder, dir_item_and_label )

def main(folder):
	read_each_file_in_folder(folder)

if __name__ == "__main__":
		main(sys.argv[1])
