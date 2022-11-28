import psycopg2

host = "cncciber.postgres.database.azure.com"
dbname = "postgres"
user = "AlejandroDuran@postgresciberfisico"
password = "noviembre2022@"
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS cnc;")
print("Finished dropping table (if existed)")

conn.commit()
cursor.close()
conn.close()