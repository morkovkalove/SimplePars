import sqlite3

conn = sqlite3.connect("titles.db")


sql = "CREATE TABLE titles(title TEXT)"
sql = "SELECT FROM * titles"
cursor = conn.cursor()



cursor.execute(sql)

result = cursor.fetchall()

for el in result:
    print(el)

conn.close()