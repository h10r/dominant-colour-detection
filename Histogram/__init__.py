import pickle
import mahotas as mh
import numpy as np    

class Histogram():
	HIST_BANDS = 128

	def from_filename(filename):
		img = mh.imread( filename )

		hist, bin_edges = np.histogram( img, bins = range(Histogram.HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		return hist

	def load_from_disk():
		try:
			return pickle.load(open("data/dict_of_histograms.bin", "rb"))
		except:
			return False