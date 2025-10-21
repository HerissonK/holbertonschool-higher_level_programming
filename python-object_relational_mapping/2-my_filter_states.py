#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database, charset='utf8')
    cur = db.cursor()

    # Use format to create the SQL query with user input
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC".format(state_name))
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
