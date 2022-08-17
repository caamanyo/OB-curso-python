import sqlite3

alumnos = [(1, 'John', 'Cleese'), (2, 'Michael', 'Palin'),
           (3, 'Terry', 'Gilliam'), (4, 'Eric', 'Idle'),
           (5, 'Graham', 'Chapman'), (6, 'Terry', 'Jones'),
           (7, 'Keith', 'Emerson'), (8, 'Freddy', 'Mercury')]

conn = sqlite3.connect('11.BBDD/escuela.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE Alumnos (id int, nombre text, apellido text)')

cursor.executemany('INSERT INTO Alumnos VALUES (?, ?, ?)', alumnos)

conn.commit()

query = cursor.execute('SELECT * FROM Alumnos WHERE nombre = "Michael"')
print(query.fetchone())

cursor.close()
conn.close()