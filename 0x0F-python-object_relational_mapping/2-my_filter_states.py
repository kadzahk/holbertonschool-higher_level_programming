#!/usr/bin/python3
"""
Write a script that takes in an
argument and displays all values in
the states table of hbtn_0e_0_usa where
name matches the argument.
"""
from sys import argv
import MySQLdb


def my_filter_states():
    """ SQL INFO FROM ARGV """
    sql_usrname = argv[1]
    sql_password = argv[2]
    sql_database = argv[3]
    usr_input = argv[4]

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
        "SELECT * FROM states WHERE name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(usr_input))

    """ FETCHING DATA """
    states = cur.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == '__main__':
    my_filter_states()
