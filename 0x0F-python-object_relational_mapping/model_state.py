#!/usr/bin/python3
"""This module defines a State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """This class defines a states table"""
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
