#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states(usr, pw, db_name):
    """This function lists the states"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         port=3306,
                         passwd=pw,
                         database=db_name)

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
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])