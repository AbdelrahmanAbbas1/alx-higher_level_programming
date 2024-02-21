#!/usr/bin/python3
"""Lists all states from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
