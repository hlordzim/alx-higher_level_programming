#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, dbname):
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    filter_states(username, password, dbname)
