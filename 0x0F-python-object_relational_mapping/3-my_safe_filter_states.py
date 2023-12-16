#!/usr/bin/python3
"""List all states where name matches the argument"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2],
                         sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("""
                SELECT * FROM states WHERE name LIKE %s
                ORDER BY states.id
                """, (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
