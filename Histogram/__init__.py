import pickle
import mahotas as mh
import numpy as np    

class Histogram():
	HIST_BANDS = 128

	def from_filename(self, filename):
		img = mh.imread( filename )

		hist, bin_edges = np.histogram( img, bins = range(self.HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		return hist

	def load_from_disk(self):
		try:
			return pickle.load(open("data/dict_of_histograms.bin", "rb"))
		except:
			return False

	"""
	def draw_all_histograms( folder_with_histograms ):
		for label in folder_with_histograms.keys():
			draw_histogram( folder_with_histograms[ label ][0], folder_with_histograms[ label ][1], label )

	def draw_histogram( histograms, bin_edges, label ):
		print("draw_histogram: " + label)
		
		for hist in histograms:
			plt.bar(bin_edges[:-1], hist, width = 1, alpha = ALPHA_BANDS)

		plt.xlim( min( bin_edges ), max( bin_edges ) )

		if SAVE_TO_FILE:
			plt.savefig("plots/" + label + ".png")
			plt.clf()
		else:
			plt.show()
			plt.clf()
	"""