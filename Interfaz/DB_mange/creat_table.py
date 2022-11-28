import psycopg2
from psycopg2 import Error

host = "cncciber.postgres.database.azure.com"
dbname = "postgres"
user = "AlejandroDuran@cncciber"
password = "Noviembre2022@"
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute("CREATE TABLE cnc (id serial PRIMARY KEY, timestamp TIMESTAMP, current FLOAT);")
print("Finished creating table")

conn.commit()
cursor.close()
conn.close()