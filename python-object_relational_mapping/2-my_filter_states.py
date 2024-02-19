#!/usr/bin/python3
"""This module defines a function that creates a connection to a SQL server"""

import MySQLdb
import sys


def print_n_state(username, password, dbase, searched):
    """This function imports a database to use"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         database=dbase)

    """Create cursor object and table name"""
    cur = db.cursor()
    table_name = "states"
    cur.execute("SELECT * FROM {0} ORDER BY {0}.id ASC;".format(table_name))

    """Access the queried data to print"""
    rows = cur.fetchall()
    for row in rows:
        if row[1] == searched:
            print(row)

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    print_n_state(sys.argv[1], sys.argv[2], sys.argv[3])