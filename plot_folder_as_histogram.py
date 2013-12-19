#!/opt/local/bin/python3.3

import os
import sys
import re

import numpy as np
import mahotas as mh

from matplotlib import pylab as plt

BINS = 16

"""
plt.title("Histogram")

if DEBUG:
	plt.show()

plt.savefig("plots/" + label + ".png")
"""

# @TODO: Make sure the graph is cleared after each folder

def read_file_and_return_histogram( a_file ):
	img = mh.imread( a_file )
	return np.histogram( img, bins=BINS, normed=True )

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

def draw_histogram( histograms_in_folder, dir_item_and_label ):
	print( histograms_in_folder[0], dir_item_and_label )

def main(folder):
	read_each_file_in_folder(folder)

if __name__ == "__main__":
		main(sys.argv[1])
