#!/usr/bin/python3
"""Prints the first state object from hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is not None:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')