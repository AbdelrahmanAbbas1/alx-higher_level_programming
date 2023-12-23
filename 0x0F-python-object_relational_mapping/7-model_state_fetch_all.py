#!/usr/bin/python3
"""Lists all State objects from databse hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        print('{}: {}'.format(state.id, state.name))
    session.close()
