#!/usr/bin/python3
"""Lists all cities from teh database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id
                """)
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
