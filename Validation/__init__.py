import glob
from operator import itemgetter

class Validation():

	FILE_PATH = "../photos/hendrik"

	def __init__(self, features, classifier):
		self.features = features
		self.classifier = classifier

		self.cross_validation()

	def cross_validation(self):
		print("cross_validation")

	def validate_with_selected_files(self):
		test_files = glob.glob( self.FILE_PATH + "/test/*" )

		for test_file in test_files:
			h = self.features.histogram_from_filename( test_file )
			
			clf_prediction = self.classifier.clf.predict_proba( h )

			unsorted_predictions = []

			print("* " + test_file.split("/")[-1] )
			for p in clf_prediction:
				for i in range(len(p)):
					if p[i] > 0.0:
						unsorted_predictions.append( [ self.classifier.colorname_by_index(i), p[i] ] )
			
			sorted_predictions = sorted( unsorted_predictions, key=itemgetter(1), reverse=True)

			for res in sorted_predictions[:3]:
				color, percentage = res
				print( color + "\t" + str(int(100*percentage)).zfill(2) + "%" )
			print()
