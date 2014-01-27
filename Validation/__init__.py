import glob
from operator import itemgetter

from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import metrics

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

class Validation():

	FILE_PATH = "../photos/hendrik"

	def __init__(self, features, classifier):
		self.features = features
		self.classifier = classifier

		self.cross_validation()

	def cross_validation(self):
		print("cross_validation")

		#self.classifier.clf.fit( self.classifier.X,self.classifier.Y )

		#cross_validation.cross_val_score( self.classifier.clf, self.classifier.X, self.classifier.Y, cv=5, scoring='f1' )

		X_train, X_test, y_train, y_test = cross_validation.train_test_split( self.classifier.X,self.classifier.Y, test_size=0.3, random_state=0 )

		print( X_train.shape )
		print( y_train.shape )
		
		print( X_test.shape )
		print( y_test.shape )

		print( "SVC: " )
		clf = SVC(gamma=0.001).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "KNeighborsClassifier: " )
		clf = KNeighborsClassifier(3).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )
		
		print( "DecisionTreeClassifier: " )
		clf = DecisionTreeClassifier(max_depth=5).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "RandomForestClassifier: " )
		clf = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "LogisticRegression: " )
		clf = LogisticRegression(C=1e5).fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "GaussianNB: " )
		clf = GaussianNB().fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

		print( "LDA: " )
		clf = LDA().fit(X_train, y_train)
		print( clf.score(X_test, y_test) )

	def validate_with_selected_files(self):
		test_files = glob.glob( self.FILE_PATH + "/test/*" )

		self.classifier.clf.fit( self.classifier.X,self.classifier.Y )

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
