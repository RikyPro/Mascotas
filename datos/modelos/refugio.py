from datos.base_de_datos import BaseDeDatos



def crear_refugio(nombre, ubicacion, mascotasenadopcion):
    crear_refugio_sql = f"""
    INSERT INTO REFUGIOS(NOMBRE, UBICACION, MASCOTASENADOPCION)
    VALUES ('{nombre}','{ubicacion}','{mascotasenadopcion}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_refugio_sql)

def modificar_refugio(nombre, ubicacion, mascotasenadopcion):
    modificar_refugio_sql = f"""
    INSERT INTO REFUGIOS(NOMBRE, UBICACION, MASCOTASENADOPCION)
    VALUES ('{nombre}','{ubicacion}','{mascotasenadopcion}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_refugio_sql)

def leer_refugio(nombre, ubicacion, mascotasenadopcion):
    leer_refugio_sql = f"""
    INSERT INTO REFUGIOS(NOMBRE, UBICACION, MASCOTASENADOPCION)
    VALUES ('{nombre}','{ubicacion}','{mascotasenadopcion}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(leer_refugio_sql)

def eliminar_refugio(nombre, ubicacion, mascotasenadopcion):
    eliminar_refugio_sql = f"""
    INSERT INTO REFUGIOS(NOMBRE, UBICACION, MASCOTASENADOPCION)
    VALUES ('{nombre}','{ubicacion}','{mascotasenadopcion}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_refugio_sql)