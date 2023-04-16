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
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE %(name)s ORDER BY states.id ASC", {'name': sys.argv[4]})

    """
    Print the results
    """
    results = cur.fetchall()

    for i, result in enumerate(results):
        if i == len(results) - 1:
            print(result[0], end="\n")
        else:
            print(result[0], end=", ")

    """
    Close all cursors
    """
    cur.close()

    """
    Close all databases
    """
    db.close()
