#!/opt/local/bin/python3.3

import numpy as np    
import matplotlib.pyplot as plt

BANDS = 20
RAND_LIMIT = 50

def generate_random_data(N):
	random_data = []

	for i in range(N):
		random_data.append( np.random.randint(RAND_LIMIT, size = BANDS) )

	return random_data

def draw_histograms(data):
	all_hist = []
	all_bin_edges = []

	for elem in data:
		hist, bin_edges = np.histogram( elem, bins = range(BANDS))
		plt.bar(bin_edges[:-1], hist, width = 1, alpha=0.1)

		all_hist.append( hist )
		all_bin_edges.append( bin_edges )

	plt.xlim( min_on_arrays( all_bin_edges ), max_on_arrays( all_bin_edges ) )

	plt.show() 

def min_on_arrays( args ):
	min_in_array = [ min(arg) for arg in args ]
	return min(min_in_array)

def max_on_arrays( args ):
	max_in_array = [ max(arg) for arg in args ]
	return max(max_in_array)

draw_histograms( generate_random_data(10) )