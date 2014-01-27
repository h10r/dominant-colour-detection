#!/opt/local/bin/python3.3

from Features import *
from Database import *
from Classifier import *
from Test import *

if __name__ == "__main__":
	f = Features()
	"""
	c = Classifier( f )

	t = Test(f, c)
	"""
	d = Database( f )
	print( d.db )

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
