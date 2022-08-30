#!/usr/bin/python3
"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
"""
from sys import argv
import MySQLdb


def filter_states():
    """ SQL INFO FROM ARGV """
    sql_usrname = argv[1]
    sql_password = argv[2]
    sql_database = argv[3]
    host = "localhost"
    port = 3306

    """ SETTING MySQLdb Connection """
    db_connection = MySQLdb.connect(
        port=port,
        host=host,
        user=sql_usrname,
        password=sql_password,
        database=sql_database)

    cur = db_connection.cursor()

    """ EXECUTING SQL QUERY """
    cur.execute(
        "SELECT id, name FROM states WHERE name\
            LIKE BINARY 'N%' ORDER BY states.id ASC")

    """ FETCHING DATA """
    states = cur.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == '__main__':
    filter_states()
