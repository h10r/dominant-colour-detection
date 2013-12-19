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

print("tonks: Generate from folder: STARTED")

def read_images_in_folder( path ):
	print("tonks: Reading folder: " + path)

	label = path.split("/")[-2]
	parent_folder = os.listdir( path )

	images = {}

	for dir_item_and_label in parent_folder: # [0:2]
		
		if path.endswith("/"):
			full_path = path + dir_item_and_label
		else:
			full_path = path + "/" + dir_item_and_label

		# for all directories in path
		if os.path.isdir( full_path ):
			dirs = os.listdir( full_path )
			
			for file_in_dir in dirs: # [0:4] - @TODO remove the 6 file limit!
				if file_in_dir.endswith(".jpg"):
					try:
						new_image = read_image_from_path( full_path + "/" + file_in_dir )

						if( dir_item_and_label in images ):
							images[dir_item_and_label].append( new_image ) 
						else:
							images[dir_item_and_label] = [ new_image ]

					except Exception:
						print("tonks: ERROR reading " + full_path + "/" + file_in_dir)
	
	if (len( images ) > 0):
		return( images )
	else:
		print("tonks: ERROR reading " + path)
		return(False)

def calculate_histograms( images ):
	hist_and_bin_edges = {}

	for label in images.keys():
		for image in images[label]:			
			hist, bin_edges = np.histogram( image, bins = range(HIST_BANDS), normed=True)
			hist = hist.clip(0.0,0.1)

			if( label in hist_and_bin_edges ):
				hist_and_bin_edges[label][0].append( hist ) 
			else:
				hist_and_bin_edges[label] = [ [hist], bin_edges ]

	return hist_and_bin_edges

def draw_all_histograms( folder_with_histograms ):
	for label in folder_with_histograms.keys():
		draw_histogram( folder_with_histograms[ label ][0], folder_with_histograms[ label ][1], label )

def draw_histogram( histograms, bin_edges, label ):
	print("tonks: draw_histogram: " + label)
	
	for hist in histograms:
		plt.bar(bin_edges[:-1], hist, width = 1, alpha = ALPHA_BANDS)

	plt.xlim( min( bin_edges ), max( bin_edges ) )

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
	dict_of_histograms = read_tonks_data_from_disk() # False

	if dict_of_histograms:
		print("tonks: Loaded histograms")
		# print( dict_of_histograms )
	else:
		all_images = read_images_in_folder( folder )		
		dict_of_histograms = calculate_histograms( all_images )
		write_tonks_data_to_disk( dict_of_histograms )

	draw_all_histograms( dict_of_histograms )

if __name__ == "__main__":
	main(sys.argv[1])

