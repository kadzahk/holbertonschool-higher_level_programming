#!/usr/bin/python3
"""
Write a script that prints the first
State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """
    Setting the session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Fecthing data
    """
    instance = session.query(State).first()
    if(instance):
        print(f"{instance.id}: {instance.name}")
    else:
        print('Nothing')
