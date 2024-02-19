#!/usr/bin/python3
"""This script lists all states from a database"""

import MySQLdb
import sys

def list_states():
    """Function that lists the states"""
    engine = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], engine=sys.argv[3])

    cursor = engine.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    engine.close()

if __name__ == "__main__":
    list_states()
