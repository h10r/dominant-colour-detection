#!/opt/local/bin/python3.3

import numpy as np
import mahotas as mh
import pylab as P

print("*** Mahotas Test ***")

filename = "/Users/hendrikheuer/Downloads/mac_wallpaper.jpg"

def read_and_generate_histogram():
	img = mh.imread( filename )
	hist, bin_edges = np.histogram( img, bins=12)

	print( hist )

def draw_histogram():
	mu, sigma = 200, 25
	x = mu + sigma*P.randn(10000)

	# the histogram of the data with histtype='step'
	n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
	P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

	# add a line showing the expected distribution
	y = P.normpdf( bins, mu, sigma)
	l = P.plot(bins, y, 'k--', linewidth=1.5)

	P.figure()

def main(filename):
	#read_and_generate_histogram( filename )

	draw_histogram()

if __name__ == "__main__":
    main(sys.argv[1])
