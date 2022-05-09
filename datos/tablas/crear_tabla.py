import sqlite3

sql_tabla_veterinaria = '''
CREATE TABLE VETERINARIAS(
IDVETERINARIA INTEGER PRIMARY KEY, 
NOMBRE TEXT,
UBICACION TEXT,
SERVICIOS TEXT 
)
'''

sql_tabla_refugio = '''
CREATE TABLE REFUGIOS(
IDREFUGIO INTEGER PRIMARY KEY, 
NOMBRE TEXT,
UBICACION TEXT,
MASCOTASENADOPCION TEXT
)
'''

sql_tabla_mascota = '''
CREATE TABLE MASCOTAS(
IDMASCOTA INTEGER PRIMARY KEY, 
NOMBRE TEXT, 
TIPOANIMAL TEXT, 
FOTO TEXT
)
'''

#sql_tabla_mascota_veterinaria = '''
#CREATE TABLE MASCOTA_VETERNIARA(
#ID_MASCOTA INTEGER PRIMARY KEY,
#ID_VETERINARIA INTEGER,
#FOREIGN KEY(ID_MASCOTA) REFERENCES MASCOTA(ID),
#FOREIGN KEY(ID_VETERINARIA) REFERENCES VETERINARIA(ID)
#)
#'''

#sql_tabla_mascota_refugio = '''
#CREATE TABLE MASCOTA_REFUGIO(
#ID_MASCOTA INTEGER PRIMARY KEY,
#ID_REFUGIO INTEGER,
#FOREIGN KEY(ID_MASCOTA) REFERENCES MASCOTA(ID),
#FOREIGN KEY(ID_REFUGIO) REFERENCES REFUGIO(ID)
#)
#'''
"""
sql_tabla_roles = '''
CREATE TABLE ROLES(
ID INTEGER PRIMARY KEY, 
TIPO TEXT
)
'''
"""

sql_tabla_usuarios = '''
CREATE TABLE USUARIOS(
ID INTEGER PRIMARY KEY,
NOMBRE TEXT,
CLAVE TEXT,
ROL TEXT
)
'''

sql_tabla_sesiones = '''
CREATE TABLE SESIONES(
 ID INTEGER PRIMARY KEY,
 ID_USUARIO TEXT,
 FECHA_HORA TEXT,
 FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO) 
)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../mascotas.db')

        print('Creando Tablas..')
        conexion.execute(sql_tabla_veterinaria)
        conexion.execute(sql_tabla_refugio)
        conexion.execute(sql_tabla_mascota)
        #conexion.execute(sql_tabla_mascota_veterinaria)
        #conexion.execute(sql_tabla_mascota_refugio)
        #conexion.execute(sql_tabla_roles)
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_sesiones)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
