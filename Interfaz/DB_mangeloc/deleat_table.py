import psycopg2
from psycopg2 import Error

host = "127.0.0.1"
port='5432'
dbname = "cnc"
user = "postgres"
password = "7b878d4842f1066bdce43d28"
sslmode = "require"

try:
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=dbname)

    cursor = connection.cursor()
    # SQL query to create a new table
    # Execute a command: this creates a new table
    cursor.execute("DROP TABLE IF EXISTS cnc;")
    connection.commit()
    print("Finished dropping table (if existed)")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")