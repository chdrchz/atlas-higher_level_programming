#!/usr/bin/python3
"""This script lists all all states from a database"""

from sqlalchemy import create_engine

username = 'user'
password = 'password'
host = 'localhost'
port = '3306'
database = 'hbtn_0e_0_usa'

"""Create the engine"""
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}', echo=True)

"""Establishes a connection to the engine"""
connection = engine.connect()

"""Executing the data query"""
result = connection.execute("SELECT * FROM states ORDER BY id ASC")

"""Fetch and print the states found"""
for row in result:
        print(row)

"""Close the connection"""
connection.close()
