es (24 sloc)  855 Bytes

#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains the class
definition of a City.
"""
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    State class:
    Attributtes:
        id = that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        name = that represents a column of a string with
        maximum 128 characters and can’t be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
