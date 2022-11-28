import psycopg2
def get_last_index():
    host = "127.0.0.1"
    port='5432'
    dbname = "cnc"
    user = "postgres"
    password = "7b878d4842f1066bdce43d28"

    
    conn = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=dbname)

    cursor = conn.cursor()
    print("Connection established")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cnc;")
    rows = cursor.fetchall()
    if len(rows)>0:
        last=rows[-1]
    else :
        last=[0]
    conn.commit()
    cursor.close()
    conn.close()
    return last

def get_all_data():
    host = "127.0.0.1"
    port='5432'
    dbname = "cnc"
    user = "postgres"
    password = "7b878d4842f1066bdce43d28"

    conn = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=dbname)

    cursor = conn.cursor()
    print("Connection established")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cnc;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows