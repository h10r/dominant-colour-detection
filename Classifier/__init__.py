import pickle
import pylab as pl

import numpy as np    

from sklearn import linear_model

class Classifier():
	H = .02

	def __init__(self, features):
		self.clf = linear_model.LogisticRegression(C=1e5)

		self.features = features

		histograms_from_disk = self.features.load_from_disk()

		self.X = []
		self.Y = []

		self.color_names = []

		if histograms_from_disk:
			self.generate( histograms_from_disk )

			self.clf.fit( self.X,self.Y )
		else:
			print("Error while initializing Classifier")

	def generate(self, dict_of_histograms):
		color_class_id = 0

		for key in dict_of_histograms.keys():			
			self.color_names.append( key )

			hists, bin_edges = dict_of_histograms[key]

			for hist in hists:
				
				if not np.all( np.isfinite( hist ) ):
					pass
				else:
					self.X.append( hist )
					self.Y.append( [color_class_id] )
				
			color_class_id = color_class_id + 1

		self.X = np.asarray( self.X , dtype=np.float64 )
		self.Y = np.asarray( self.Y , dtype=np.float64 )

		self.Y = np.ravel( self.Y )

	def colorname_by_index( self, index ):
		return self.color_names[ index ]

	def predict_from_histogram(self, histogram):
		return self.clf.predict_proba( histogram )
	
	def predict_from_filename(self, filename):
		return self.predict_from_histogram( self.features.histogram_from_filename( filename ) )

