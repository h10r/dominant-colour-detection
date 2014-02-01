import sys
import pickle
import csv

import mahotas as mh
import numpy as np    

class DataSource():
	HIST_BANDS = 8

	HIST_CLIPPING_MIN = 0.0
	HIST_CLIPPING_MAX = 1.0

	USE_CACHED_VERSION = True
	
	PATH_TO_SOURCE_FILES = "../photos/zalando/"

	#PATH_TO_DATA_SOURCE = "data/clothes_test.csv"
	PATH_TO_DATA_SOURCE = "data/clothes.csv"

	def __init__(self):

		if self.USE_CACHED_VERSION:
			self.db = self.load_db_from_cache()
		else:
			self.db = {}
			self.load_from_csv()
			self.save_db_to_cache()

	def histogram_from_filename(self, filename):
		img = np.reshape( mh.imread( filename ), (-1,3))

		r = img[:,0]
		g = img[:,1]
		b = img[:,2]

		r_hist, r_bin_edges = np.histogram( r, bins = range(self.HIST_BANDS), density=True )
		g_hist, g_bin_edges = np.histogram( g, bins = range(self.HIST_BANDS), density=True )
		b_hist, b_bin_edges = np.histogram( b, bins = range(self.HIST_BANDS), density=True )

		feature_vector = r_hist + g_hist + b_hist
		feature_vector = feature_vector.clip( 0.0, 0.1 )

		return feature_vector

	def load_db_from_cache(self):
		try:
			return pickle.load(open("data/cached_db.bin", "rb"))
		except:
			return False
	
	def save_db_to_cache(self):
		try:
			return pickle.dump( self.db, open( "data/cached_db.bin", "wb" ) )
		except:
			return False

	def load_from_csv(self):
		with open( self.PATH_TO_DATA_SOURCE , 'rt') as f:
			reader = csv.reader(f)
			try:
				for row in reader:
					filename,colors = row[0].split(";")
					self.generate_histograms_from_filename_and_categorize_by_color( filename,colors )
			except csv.Error as e:
				sys.exit( 'file %s, line %d: %s' % ( self.PATH_TO_DATA_SOURCE, reader.line_num, e) )

	def generate_histograms_from_filename_and_categorize_by_color( self,filename,colors ):
		print("** generate_histograms_from_filename_and_categorize_by_color " + filename)
		for color in colors.split(","):
			if ( len(color) > 0 ):
				histograms = self.histogram_from_filename( self.PATH_TO_SOURCE_FILES + filename )

				if( color in self.db ):
					self.db[color].append( histograms ) 
				else:
					self.db[color] = [ histograms ]

