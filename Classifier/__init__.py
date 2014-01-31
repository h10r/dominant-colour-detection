import pickle
import pylab as pl

import numpy as np    

from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import metrics

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.lda import LDA

class Classifier():
	def __init__(self, data_source):
		self.data_source = data_source

		self.X = []
		self.Y = []

		self.color_names = []

		self.generate( self.data_source.db )
			
		self.cross_validation()
		
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

	def cross_validation(self):
		print("** cross_validation start")

		X_train, X_test, y_train, y_test = cross_validation.train_test_split( self.classifier.X,self.classifier.Y, test_size=0.3, random_state=0 )

		print( "SVC: " )
		clf = SVC().fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "LogisticRegression: " )
		clf = LogisticRegression(C=1e5).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "LDA: " )
		clf = LDA().fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print("** cross_validation finished")

	def colorname_by_index( self, index ):
		return self.color_names[ index ]

	"""
	def predict_from_histogram(self, histogram):
		return self.clf.predict_proba( histogram )
	
	def predict_from_filename(self, filename):
		return self.predict_from_histogram( self.data_source.histogram_from_filename( filename ) )
	"""
