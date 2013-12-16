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

def draw_histogram( x, label, DEBUG=False ):
	# the histogram of the data with histtype='step'
	n, bins, patches = plt.hist(x, 50, normed=True, histtype='step')
	plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

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

	x = []

	parent_folder = os.listdir( path )

	for dir_item_and_label in parent_folder:
		full_path = path + "/" + dir_item_and_label

		# for all directories in path
		if os.path.isdir( full_path ):
			# print("is path " + full_path + " - label: " + dir_item_and_label)

			dirs = os.listdir( full_path )

			for file_in_dir in dirs[0:5]:
				if file_in_dir.endswith(".jpg"):
					try:
						hist, bin_edges = read_and_generate_histogram( full_path + "/" + file_in_dir )
						x.append( hist )
					except Exception:
						print("plot_folder_as_histogram: ERROR reading " + full_path + "/" + file_in_dir)

			draw_histogram(x, dir_item_and_label)

def main(folder):
	read_each_file_in_folder(folder)

if __name__ == "__main__":
		main(sys.argv[1])
