import sqlite3

class Database():
	PATH_OF_DATABASE = "data/mcgill_plus_hendrik.db"

	def __init__(self, features):
		self.features = features

		conn = sqlite3.connect( self.PATH_OF_DATABASE )
		self.c = conn.cursor()

		self.db = {}

		self.load_from_database()

	def load_from_database(self):
		self.c.execute("SELECT * FROM images LIMIT 0,3")
		images_in_database = self.c.fetchall()

		for db_img in images_in_database:
			nr,filename,colors,tags = db_img
			
			self.save_histograms_based_on_color( filename,colors )

	def save_histograms_based_on_color( self,filename,colors ):
		for color in colors.split(","):
			if ( len(color) > 0 ):
				histogram = self.features.histogram_from_filename( filename )

				if( color in self.db ):
					self.db[color].append( histogram ) 
				else:
					self.db[color] = [ histogram ]