import mysql.connector
import sys

line = input()

CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password":"1234",
    "database":"study"
}

cnx = mysql.connector.connect(**CONFIG)
cur = cnx.cursor(buffered=True)

inputName = (line,)

sql = "SELECT id, name, tel FROM user where name=%s"
cur.execute(sql,inputName)

rows = cur.fetchall()

if len(rows):
    print("id\tname\ttel")
    for (id, name, tel) in rows:
        print(id, name, tel, sep="\t")
else:
    print("no rows")

cur.close()
cnx.close()
