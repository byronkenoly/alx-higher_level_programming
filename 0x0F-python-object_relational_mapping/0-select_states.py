#!/usr/bin/python3

import MySQLdb
import sys

"""
Connecting to MySQL database
"""
db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])

"""
Cursor object that allows one to interact with the
MySQL database by executing queries and retrieving results
"""
cur = db.cursor()

"""
Executing MySQL queries
"""
all_states = cur.execute("SELECT * FROM states")

"""
Print the results
"""
results = cur.fetchall()

for result in results:
    print(result)

"""
Close all cursors
"""
cur.close()

"""
Close all databases
"""
db.close()

