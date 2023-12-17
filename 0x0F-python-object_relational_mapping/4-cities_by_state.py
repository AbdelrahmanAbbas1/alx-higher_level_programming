#!/usr/bin/python3
"""List all cities from the database"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2],
                         sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("""
                SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id
                """)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
