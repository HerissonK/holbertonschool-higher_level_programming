#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import sys
import MySQLdb


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * \
                    FROM `states` \
                    WHERE BINARY `name` = '{}' \
                    ORDER BY id".format(argv[4]))

    for state in cursor.fetchall():
        print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()
