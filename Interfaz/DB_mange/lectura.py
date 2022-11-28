import psycopg2
def get_last_index():
    host = "postgresciberfisico.postgres.database.azure.com"
    dbname = "postgres"
    user = "mariogtz5@postgresciberfisico"
    password = "Ciberfisicos2022"
    sslmode = "require"

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
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
    host = "postgresciberfisico.postgres.database.azure.com"
    dbname = "postgres"
    user = "mariogtz5@postgresciberfisico"
    password = "Ciberfisicos2022"
    sslmode = "require"

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cnc;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows