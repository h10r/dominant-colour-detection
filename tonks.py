#!/opt/local/bin/python3.3

import os
import sys
import re
import numpy as np    
import mahotas as mh
import matplotlib.pyplot as plt

HIST_BANDS = 128
ALPHA_BANDS = 0.1
SAVE_TO_FILE = True

def read_each_file_in_folder( path ):
	print("tonks: Reading folder: " + path)

	label = path.split("/")[-2]

	parent_folder = os.listdir( path )

	for dir_item_and_label in parent_folder: # [0:2]
		full_path = path + "/" + dir_item_and_label

		# for all directories in path
		if os.path.isdir( full_path ):
			dirs = os.listdir( full_path )
			images_in_path = []

			for file_in_dir in dirs: # [0:3] - @TODO remove the 6 file limit!

				if file_in_dir.endswith(".jpg"):
					try:
						images_in_path.append( read_image_from_path( full_path + "/" + file_in_dir ) )
					except Exception:
						print("tonks: ERROR reading " + full_path + "/" + file_in_dir)

			print("tonks: STATS: " + dir_item_and_label + ": " + str(len( images_in_path )))

			draw_histograms( images_in_path, dir_item_and_label )

def generate_random_data(N):
	RAND_LIMIT = 50

	random_data = []

	for i in range(N):
		random_data.append( np.random.randint(RAND_LIMIT, size = BANDS) )

	return random_data

def draw_histograms(data, label):
	all_hist = []
	all_bin_edges = []

	for elem in data:
		hist, bin_edges = np.histogram( elem, bins = range(HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		plt.bar(bin_edges[:-1], hist, width = 1, alpha = ALPHA_BANDS)

		all_hist.append( hist )
		all_bin_edges.append( bin_edges )

	plt.xlim( min_on_arrays( all_bin_edges ), max_on_arrays( all_bin_edges ) )

	if SAVE_TO_FILE:
		plt.savefig("plots/" + label + ".png")
		plt.clf()
	else:
		plt.show()
		plt.clf()

#### HELPER FUNCTIONS ####

def read_image_from_path( image ):
	img = mh.imread( image )
	#small_img = mh.imresize( mh.imread( image ), 0.1 )
	return img

def min_on_arrays( args ):
	min_in_array = [ min(arg) for arg in args ]
	return min(min_in_array)

def max_on_arrays( args ):
	max_in_array = [ max(arg) for arg in args ]
	return max(max_in_array)

#### MAIN ####

def main(folder):
	read_each_file_in_folder(folder)

if __name__ == "__main__":
		main(sys.argv[1])

