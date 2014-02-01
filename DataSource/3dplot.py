import mahotas as mh
import numpy as np    

HIST_BANDS = 32

img = mh.imread( "/Users/hendrikheuer/Projects/dominant-colour-detection/photos/zalando/AD121D06S-502@5.1.jpg" )

img = np.reshape(img, (-1,3))

r = img[:,0]
g = img[:,1]
b = img[:,2]

"""
print( r )
print( "----------------" )
print( g )
print( "----------------" )
print( b )
print( "----------------" )
"""

r_hist, r_bin_edges = np.histogram( r, bins = range(HIST_BANDS), normed=True)
g_hist, g_bin_edges = np.histogram( g, bins = range(HIST_BANDS), normed=True)
b_hist, b_bin_edges = np.histogram( b, bins = range(HIST_BANDS), normed=True)

HIST_CLIPPING_MIN = 0.0
HIST_CLIPPING_MAX = 1.0

r_hist = r_hist.clip( HIST_CLIPPING_MIN, HIST_CLIPPING_MAX )
g_hist = g_hist.clip( HIST_CLIPPING_MIN, HIST_CLIPPING_MAX )
b_hist = b_hist.clip( HIST_CLIPPING_MIN, HIST_CLIPPING_MAX )

print( r_hist )
print( g_hist )
print( b_hist )
