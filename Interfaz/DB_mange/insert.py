import psycopg2
from io import StringIO
def insertar(tuples):
    host = "cncciber.postgres.database.azure.com"
    dbname = "postgres"
    user = "AlejandroDuran@postgresciberfisico"
    password = "noviembre2022@"
    sslmode = "require"

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    i=1
    cursor = conn.cursor()
    #for x in tuples:
    cursor.execute("INSERT INTO cnc (timestamp, current) VALUES (%s, %s);", tuples)
        #print(i)
        #i=i+1
    print('Se inserto correctamente')
    conn.commit()
    cursor.close()
    conn.close()
def execute_many(df, table):
    host = "cncciber.postgres.database.azure.com"
    dbname = "postgres"
    user = "AlejandroDuran@postgresciberfisico"
    password = "noviembre2022@"
    sslmode = "require"

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_many() done")
    cursor.close()
    
def copy_from_stringio(df, table):
    host = "cncciber.postgres.database.azure.com"
    dbname = "postgres"
    user = "AlejandroDuran@postgresciberfisico"
    password = "noviembre2022@"
    sslmode = "require"
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index_label='Date-time', header=False)
    buffer.seek(0)
    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("Upload done")
    cursor.close()
    conn.close()