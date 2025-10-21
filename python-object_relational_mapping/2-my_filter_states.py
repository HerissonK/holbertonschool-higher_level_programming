#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Escape single quotes to handle edge cases
    state_name_escaped = state_name.replace("'", "\\'")

    # Connect to MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=username, passwd=password, db=database,
                           charset='utf8')
    cur = conn.cursor()

    # Case-sensitive exact match using BINARY
    query = ("SELECT * FROM states WHERE name = BINARY '{}' "
             "ORDER BY id ASC".format(state_name_escaped))
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
