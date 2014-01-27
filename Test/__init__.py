class Test():

	def __init__(self, clf):
		self.clf = clf

		self.test_with_selected_files()

	def test_with_selected_files():
		test_files = glob.glob( FILE_PATH + "/test/*" )

		for test_file in test_files:
			h = Histogram.get_histogram_from_image( test_file )
			
			clf_predict = clf.predict_proba( h )

			unsorted_predictions = []

			print("* " + test_file.split("/")[-1] )
			for p in clf_predict:
				for i in range(len(p)):
					if p[i] > 0.0:
						unsorted_predictions.append( [ self.clf.colorname_by_index(i), p[i] ] )
			
			sorted_predictions = sorted( unsorted_predictions, key=itemgetter(1), reverse=True)

			for res in sorted_predictions[:3]:
				color, percentage = res
				print( color + "\t" + str(int(100*percentage)).zfill(2) + "%" )
			print()
