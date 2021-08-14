import os
import sqlite3

class DatabaseHandler():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def create_person(self, username: str, password: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO Person (username, password) VALUES ('{username}', '{password}');"
		cursor.execute(query)
		cursor.close()
		self.con.commit()
