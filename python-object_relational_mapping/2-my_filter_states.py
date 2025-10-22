#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument.
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = db.cursor()

    # Use format to create the SQL query with the user input
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
