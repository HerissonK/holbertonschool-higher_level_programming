#!/usr/bin/python3
"""
write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument. But this time, write one
that is safe from MySQL injections!
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

    # Escape single quotes to prevent syntax errors
    safe_name = state_name.replace("'", "''")

    # Required: use format(), not %s
    query = ("SELECT * FROM states WHERE name = BINARY '{}' "
             "ORDER BY id ASC".format(safe_name))
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
