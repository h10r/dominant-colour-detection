#!/opt/local/bin/python3.3

from Database import *
from Histogram import *
from Classifier import *
from Test import *

if __name__ == "__main__":
	"""
	h = Histogram()
	c = Classifier( h )

	t = Test(h, c)
	"""
	d = Database()
	print( d.fetch_all() )

"""
def main():

	if GENERATE_FILES:
		clf = generate_and_return_classifier()
		write_classifier_to_disk( clf )
	else:
		clf = load_classifier_from_disk()
	
	if clf:
		direct_test()
	else:
		print("ERROR: couldn't find classifier")
"""
