#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states():
    """This function lists the states"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")

    """Print the queried data"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    """Close connection and cursor object"""
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()