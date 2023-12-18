#!/usr/bin/python3
"""List all cities of a certain state as an argument from the database"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2],
                         sys.argv[3], 3306)
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                """, (sys.argv[4],))
    states = cur.fetchall()
    state = list(row[0] for row in states)
    print(*state, sep=", ")

    cur.close()
    db.close()
