#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state,
using the database
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 5:
        sys.exit('Use: 5-filter_cities.py <mysql username> <mysql password>'
                 ' <database name> <state name>')

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states "
                "ON cities.state_id = states.id WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4], ))
    query_rows = cur.fetchall()
    cities = [row[0] for row in query_rows]
    print(', '.join(cities))
    cur.close()
    conn.close()