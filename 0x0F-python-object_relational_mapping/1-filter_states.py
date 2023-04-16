#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
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
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC")

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
