#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


def cities_by_state():
    """ SQL INFO FROM ARGV """
    sql_usrname = argv[1]
    sql_password = argv[2]
    sql_database = argv[3]
    sql_state_name = argv[4]

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

    """ EXECUTING SQL QUERY"""
    cur.execute(
        """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (sql_state_name, ))

    """ FETCHING DATA """
    cities = cur.fetchall()

    printed = [citie[0] for citie in cities]
    print(', '.join(printed))

    db_connection.close()


if __name__ == '__main__':
    cities_by_state()
