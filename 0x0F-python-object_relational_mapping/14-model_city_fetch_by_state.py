#!/usr/bin/python3
"""Prints all City objects from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(State.name, City.id, City.name).join
              (State, State.id == City.state_id).all())
    for city in cities:
        print('{}: ({}) {}'.format(city[0], city[1], city[2]))
