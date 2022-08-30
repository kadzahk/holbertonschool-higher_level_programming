#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains the class
definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class:
    Attributtes:
        id = that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        name = that represents a column of a string with
        maximum 128 characters and can’t be null
        state_id = that represents a column of an integer,
        can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
