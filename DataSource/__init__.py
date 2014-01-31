import sys
import pickle
import csv

import mahotas as mh
import numpy as np    

class DataSource():
	HIST_BANDS = 128

	USE_CACHED_VERSION = False
	USE_SMALL_TEST_SET = False

	PATH_TO_SOURCE_FILES = "../photos/zalando/"

	if USE_SMALL_TEST_SET:
		PATH_TO_DATA_SOURCE = "data/clothes.csv"
	else:
		PATH_TO_DATA_SOURCE = "data/clothes_test.csv"

	def __init__(self):

		if self.USE_CACHED_VERSION:
			self.db = self.load_db_from_cache()
		else:
			self.db = {}
			self.load_from_csv()
			self.save_db_to_cache()

	def histogram_from_filename(self, filename):
		img = mh.imread( filename )

		hist, bin_edges = np.histogram( img, bins = range(self.HIST_BANDS), normed=True)
		hist = hist.clip(0.0,0.1)

		return hist

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
				histogram = self.histogram_from_filename( self.PATH_TO_SOURCE_FILES + filename )

				if( color in self.db ):
					self.db[color].append( histogram ) 
				else:
					self.db[color] = [ histogram ]

