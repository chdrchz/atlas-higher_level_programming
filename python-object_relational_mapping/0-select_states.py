#!/usr/bin/python3
"""This script that lists all states from a database"""

import MySQLdb
import sys

def list_states():
    """This function will establish the connection, and list states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    """Create a cursor object and query the data"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    """Print data"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    """Close cursor and engine"""
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()
