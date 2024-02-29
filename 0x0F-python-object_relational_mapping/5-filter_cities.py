#!/usr/bin/python3
"""List all cities of the state when passed as an argument"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name FROM cities
                LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                """, (sys.argv[4],))
    cities = cur.fetchall()
    city = list(row[0] for row in cities)
    print(*city, sep=", ")
    cur.close()
    db.close()
