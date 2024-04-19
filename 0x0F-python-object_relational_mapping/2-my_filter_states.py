#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, dbname, search_name):

    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=dbname)
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search_name,))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    search_name = sys.argv[4]

    filter_states(username, password, dbname, search_name)OA
