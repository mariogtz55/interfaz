import psycopg2
from io import StringIO

def copy_from_stringio(df, table):
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
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index_label='Date-time', header=False)
    buffer.seek(0)

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