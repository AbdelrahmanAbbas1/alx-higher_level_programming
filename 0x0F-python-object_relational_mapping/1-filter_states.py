#!/usr/bin/python3
"""List all states with a name starting with N from hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2],
                         sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE LEFT(name, 1) = "N"')
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
