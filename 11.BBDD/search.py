import sqlite3

conn = sqlite3.connect('11.BBDD/escuela.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM Alumnos WHERE nombre = "Michael"')
print(query.fetchone())

cursor.close()
conn.close()