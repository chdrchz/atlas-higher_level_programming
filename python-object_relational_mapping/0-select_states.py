#!/usr/bin/python3
"""This script lists all all states from a database"""

import MySQLdb
import sys

"""Create an engine"""
engine= MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], engine=sys.argv[3])

"""Create a cursor object"""
cursor = engine.cursor()

"""Query the data to find all states"""
cursor.execute("SELECT * FROM states ORDER BY id")

"""Fetch all data from result set"""
rows = cursor.fetchall()

"""Print the rows"""
for row in rows:
    print(row)

cursor.close()
engine.close()
