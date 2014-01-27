import sqlite3

class Database():
	def __init__(self):
		conn = sqlite3.connect('data/mcgill_plus_hendrik.db')
		self.c = conn.cursor()

	def fetch_all(self):
		self.c.execute("SELECT * FROM images")
		return self.c.fetchall()