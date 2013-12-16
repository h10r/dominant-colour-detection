#!/opt/local/bin/python3.3

import sys
import numpy as np
import mahotas as mh

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

print
print("*** Mahotas Test ***")
print

filename = "/Users/hendrikheuer/Downloads/mac_wallpaper.jpg"

def read_and_generate_histogram():
	img = mh.imread( filename )
	hist, bin_edges = np.histogram( img, bins=12)

	print( hist )

def draw_histogram():
	mu, sigma = 200, 25
	x = mu + sigma*np.random.randn(10000)

	# the histogram of the data with histtype='step'
	n, bins, patches = plt.hist(x, 50, normed=1, histtype='stepfilled')
	plt.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

	# add a line showing the expected distribution
	y = mlab.normpdf( bins, mu, sigma)
	l = plt.plot(bins, y, 'k--', linewidth=1.5)

	#plt.plot(range(10), range(10))
	plt.title("Simple Plot")
	plt.show()

def main(filename):
	#read_and_generate_histogram( filename )

	draw_histogram()

if __name__ == "__main__":
    main(sys.argv[1])
