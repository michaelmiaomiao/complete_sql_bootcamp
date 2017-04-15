import psycopg2
import sys
import pprint

def main():
    conn_string = "host='localhost' dbname='dvdrental' user='cohara' password='password'"
    print("Connecting to database: " + conn_string)

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment;")
    records = cursor.fetchall()

    pprint.pprint(records)

if __name__ == "__main__":
    main()
