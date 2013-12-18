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

def read_images_in_folder( path ):
	print("tonks: Reading folder: " + path)

	label = path.split("/")[-2]
	parent_folder = os.listdir( path )

	for dir_item_and_label in parent_folder: # [0:2]
		full_path = path + "/" + dir_item_and_label

		images_in_path = []

		# for all directories in path
		if os.path.isdir( full_path ):
			dirs = os.listdir( full_path )
			
			for file_in_dir in dirs: # [0:3] - @TODO remove the 6 file limit!
				if file_in_dir.endswith(".jpg"):
					try:
						images_in_path.append( ( read_image_from_path( full_path + "/" + file_in_dir ), dir_item_and_label ) )
					except Exception:
						print("tonks: ERROR reading " + full_path + "/" + file_in_dir)
	
	if (len(images_in_path) > 0):
		return(images_in_path)
	else:
		print("tonks: ERROR reading " + path)
		return(False)

def calculate_histograms(image_and_label):
	hist_and_bin_edges_and_label = []

	for elem in image_and_label:
		image,label = elem
		
		hist, bin_edges = np.histogram( image, bins = range(HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		hist_and_bin_edges_and_label.append( ( hist, bin_edges, label ) )

	return hist_and_bin_edges_and_label

def draw_histograms( hist_and_bin_edges_and_label ):

	for elem in hist_and_bin_edges_and_label:
		
		hist, bin_edges, label = elem

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

def read_tonks_data_from_disk():
	try:
		return pickle.load(open("tonks.dat", "rb"))
	except:
		return False

def write_tonks_data_to_disk( tonks_data ):
	print("tonks: Save data to disk")
	pickle.dump( tonks_data, open("tonks.dat", "wb"))
	
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

#### TEST DATA ####

def generate_random_data(N):
	RAND_LIMIT = 50

	random_data = []

	for i in range(N):
		random_data.append( np.random.randint(RAND_LIMIT, size = BANDS) )

	return random_data

#### MAIN ####

def main(folder):
	hist_and_bin_edges_and_label = read_tonks_data_from_disk()

	if hist_and_bin_edges_and_label:
		print("tonks: Loaded histograms")
		print( hist_and_bin_edges_and_label )
	else:
		all_images = read_images_in_folder( folder )
		hist_and_bin_edges_and_label = calculate_histograms( all_images )

		write_tonks_data_to_disk( hist_and_bin_edges_and_label )

if __name__ == "__main__":
		main(sys.argv[1])

