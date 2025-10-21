#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connexion à la base MySQL
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=username, passwd=password,
                               db=db_name, charset="utf8")

        # Création du curseur
        cur = conn.cursor()

        # Exécution de la requête pour récupérer tous les états
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Affichage des résultats
        for row in cur.fetchall():
            print(row)

        # Fermeture du curseur et de la connexion
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
