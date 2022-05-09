from datos.base_de_datos import BaseDeDatos



def crear_veterinaria(nombre, ubicacion, servicios):
    crear_veterinaria_sql = f"""
    INSERT INTO VETERINARIAS(NOMBRE, UBICACION, SERVICIOS)
    VALUES ('{nombre}','{ubicacion}','{servicios}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_veterinaria_sql)

def modificar_veterinaria(nombre, ubicacion, servicios):
    modificar_veterinaria_sql = f"""
    INSERT INTO VETERINARIAS(NOMBRE, UBICACION, SERVICIOS)
    VALUES ('{nombre}','{ubicacion}','{servicios}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_veterinaria_sql)

def leer_veterinaria(nombre, ubicacion, servicios):
    leer_veterinaria_sql = f"""
    INSERT INTO VETERINARIAS(NOMBRE, UBICACION, SERVICIOS)
    VALUES ('{nombre}','{ubicacion}','{servicios}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(leer_veterinaria_sql)

def eliminar_veterinaria(nombre, ubicacion, servicios):
    eliminar_veterinaria_sql = f"""
    INSERT INTO VETERINARIAS(NOMBRE, UBICACION, SERVICIOS)
    VALUES ('{nombre}','{ubicacion}','{servicios}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_veterinaria_sql)