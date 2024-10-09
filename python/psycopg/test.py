import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to default db and create a test db
conn = psycopg2.connect(dbname = 'postgres', user = "postgres", host = "localhost", port = 5432)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("test")))

#close connection to default db
cursor.close()
conn.close()

#connect to test db
conn = psycopg2.connect(dbname = 'test', user = "postgres", host = "localhost", port = 5432)
cursor = conn.cursor()

#create test table
query = sql.SQL("CREATE TABLE {} ( {} SERIAL PRIMARY KEY, {} VARCHAR NOT NULL, {} INT );").format(
        sql.Identifier("person"),
        sql.Identifier("pers_id"),
        sql.Identifier("pers_name"),
        sql.Identifier("pers_age"))
cursor.execute(query)

#create some data
x = 1
for name in ("eric", "bill", "mike", "tim", "paul", "peter", "jim"):
    query = sql.SQL("INSERT INTO {} ({}, {}) VALUES ({}, {});").format(
            sql.Identifier("person"),
            sql.Identifier("pers_name"),
            sql.Identifier("pers_age"),
            sql.Literal(name),
            sql.Literal(x + 15))
    cursor.execute(query)
    x += 1

#get some data
query = sql.SQL("SELECT * FROM {};").format(sql.Identifier("person"))
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(f"pers_id {record[0]} pers_name {record[1]} pers_age {record[2]}")

#delete data
query = sql.SQL("DELETE FROM {};").format(sql.Identifier("person"))
cursor.execute(query)

conn.commit()

#close connection to test db
cursor.close()
conn.close()

#connect to default db to drop test db
conn = psycopg2.connect(dbname = 'postgres', user = "postgres", host = "localhost", port = 5432)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute(sql.SQL("DROP DATABASE {};").format(sql.Identifier("test")))

conn.commit()
cursor.close()
conn.close()
