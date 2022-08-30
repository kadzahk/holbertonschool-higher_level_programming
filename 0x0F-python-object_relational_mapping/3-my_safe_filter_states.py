#!/usr/bin/python3
"""
Wait, do you remember the previous task?
Did you test "Arizona'; TRUNCATE TABLE states
; SELECT * FROM states WHERE name = '"
as an input?
"""
from sys import argv
import MySQLdb


def my_safe_filter_states():
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

    """ EXECUTING SQL QUERY
    ('\') Scape characteres the real Query executed is =
    b"SELECT * FROM states WHERE name = 'Arizona\\'; TRUNCATE
    TABLE states ; SELECT * FROM states WHERE name = \\''" """

    cur.execute("SELECT * FROM states WHERE name = %s", (usr_input, ))

    """ FETCHING DATA """
    states = cur.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == '__main__':
    my_safe_filter_states()
