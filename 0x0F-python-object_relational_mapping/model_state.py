#!/usr/bin/python3
"""This module defines a class of a State and an instance of Base"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class State(Base):
    """This class defines a State table"""

    __tablename__ = 'states'

    id = Column(Integer, unique=True,
                nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
