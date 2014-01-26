#!/opt/local/bin/python3.3

import sqlite3

PATH_OF_DATABASE = "data/mcgill_plus_hendrik.db"

database = sqlite3.connect( PATH_OF_DATABASE )

c = database.cursor()
c.execute('SELECT * FROM images')

images_in_database = c.fetchall()

print( images_in_database[0] )
