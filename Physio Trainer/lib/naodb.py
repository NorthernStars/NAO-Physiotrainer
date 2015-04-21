'''
Python module for SQLite3 databse querys.
'''
import sqlite3
	
# Gets SQL query from sqlite3 database file.
# Returns result array or None.
def sqlQuery(databasefile, query):

	if type(databasefile) is str:
		dbconnection = sqlite3.connect(databasefile)
		if dbconnection:
			db = dbconnection.cursor()
		
			if db and type(query) is str and len(query) > 0:
				# execute query and get results
				db.execute(query)
				ret = db.fetchall()
		
				# commit changed, close database and return results
				dbconnection.commit()
				dbconnection.close()
				return ret
	
	return None
