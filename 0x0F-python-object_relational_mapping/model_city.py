#!/usr/bin/python3
"""This module defines a City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """This class represents a city"""
    __tablename__ = 'cities'

    id = Column(Integer, unique=True,
                nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
