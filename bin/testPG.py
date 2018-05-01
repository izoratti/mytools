import psycopg2

try:
    connect_str = "user='foglamp' dbname='foglamp'"
    # connect_str = "user='foglamp' dbname='foglamp' host='/tmp/'"
    # connect_str = "host='127.0.0.1' user='foglamp' dbname='foglamp'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * from foglamp.configuration")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect!")
    print(e)
