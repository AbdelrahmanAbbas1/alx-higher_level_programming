#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT * FROM states
                WHERE name LIKE 'N%'
                """)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
