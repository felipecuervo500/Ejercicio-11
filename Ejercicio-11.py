import sqlite3

conexion1 = sqlite3.connect("base2.db")

miCursor = conexion1.cursor()
miCursor.execute("CREATE TABLE ALUMNOS8 (ID INTEGER, NOMBRE VARCHAR(30), APELLIDO VARCHAR(30))")

misAlumnos = [

    (101, "Andres", "Acosta"),
    (102, "Maria", "Benitez"),
    (103, "Eduardo", "Cuervo"),
    (104, "Nefertiti", "Johnson"),
    (105, "Ayrton", "Mendoza"),
    (106, "Laika", "Osorio"),
    (107, "Bernie", "Rondon"),
    (108, "Hornie", "Sepulveda")

]

miCursor.executemany("INSERT INTO ALUMNOS8 VALUES (?,?,?)", misAlumnos)

conexion1.commit()

miCursor.execute("SELECT * FROM ALUMNOS8 WHERE ID=101")
ALUMNOS8 = miCursor.fetchone()
print(ALUMNOS8)

conexion1.close()
