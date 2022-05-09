from datos.modelos import usuario as modelo_usuario
#from datos.modelos import mascota as modelomascota
#from datos.modelos import veterinaria as modeloveterinaria
#from datos.modelos import refugio as modelorefugio
from datetime import datetime

class UserNotFound(Exception):
    pass

def _existe_usuario(nombre, clave):
    usuarios = modelo_usuario.obtener_usuarios_por_nombre_clave(nombre, clave)
    return not len(usuarios) == 0


def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(id_usuario, dt_string)


def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()


def obtener_usuario(id_usuario):
    usuarios = modelo_usuario.obtener_usuario(id_usuario)
    if len(usuarios) == 0:
        raise UserNotFound("El usuario no existe")
    return usuarios[0]

def crear_usuario(nombre, clave):
    if not _existe_usuario(nombre, clave):
        modelo_usuario.crear_usuario(nombre, clave)
    else:
        raise Exception("El usuario ya existe")

def modificar_usuario(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)

def borrar_usuario(id_usuario):
    modelo_usuario.borrar_usuario(id_usuario)


def login(nombre, clave):
    if _existe_usuario(nombre, clave):
        usuario = modelo_usuario.obtener_usuarios_por_nombre_clave(nombre, clave)[0]
        return _crear_sesion(usuario['id'])
    else:
        raise UserNotFound("El usuario no existe o la clave es invalida")


def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True


"""
def crear_mascota(nombre, tipoanimal, foto):
    modelomascota.crear_mascota(nombre, tipoanimal, foto)

def modificar_mascota(nombre, tipoanimal, foto):
    modelomascota.modificar_mascota(nombre, tipoanimal, foto)

def leer_mascota(nombre, tipoanimal, foto):
    modelomascota.leer_mascota(nombre, tipoanimal, foto)

def eliminar_mascota(nombre, tipoanimal, foto):
    modelomascota.eliminar_mascota(nombre, tipoanimal, foto)


def crear_veterinaria(nombre, ubicacion, servicios):
    modeloveterinaria.crear_veterinaria(nombre, ubicacion, servicios)

def modificar_veterinaria(nombre, ubicacion, servicios):
    modeloveterinaria.modificar_veterinaria(nombre, ubicacion, servicios)

def leer_veterinaria(nombre, ubicacion, servicios):
    modeloveterinaria.leer_veterinaria(nombre, ubicacion, servicios)

def eliminar_veterinaria(nombre, ubicacion, servicios):
    modeloveterinaria.eliminar_veterinaria(nombre, ubicacion, servicios)


def crear_refugio(nombre, ubicacion, mascotasenadopcion):
    modelorefugio.crear_refugio(nombre, ubicacion, mascotasenadopcion)

def modificar_refugio(nombre, ubicacion, mascotasenadopcion):
    modelorefugio.modificar_refugio(nombre, ubicacion, mascotasenadopcion)

def leer_refugio(nombre, ubicacion, mascotasenadopcion):
    modelorefugio.leer_refugio(nombre, ubicacion, mascotasenadopcion)

def eliminar_refugio(nombre, ubicacion, mascotasenadopcion):
    modelorefugio.eliminar_refugio(nombre, ubicacion, mascotasenadopcion)
"""