#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 5:
        sys.exit('Use: 1-filter_states.py <mysql username> <mysql password>'
                 ' <database name> <state name searched>')
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY "
                "'{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()