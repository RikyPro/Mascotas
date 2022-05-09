from datos.base_de_datos import BaseDeDatos



def crear_mascota(nombre, tipoanimal, foto):
    crear_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, TIPOANIMAL, FOTO)
    VALUES ('{nombre}','{tipoanimal}','{foto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_mascota_sql)

def modificar_mascota(nombre, tipoanimal, foto):
    modificar_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, TIPOANIMAL, FOTO)
    VALUES ('{nombre}','{tipoanimal}','{foto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_mascota_sql)

def leer_mascota(nombre, tipoanimal, foto):
    leer_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, TIPOANIMAL, FOTO)
    VALUES ('{nombre}','{tipoanimal}','{foto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(leer_mascota_sql)

def eliminar_mascota(nombre, tipoanimal, foto):
    eliminar_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, TIPOANIMAL, FOTO)
    VALUES ('{nombre}','{tipoanimal}', '{foto}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_mascota_sql)