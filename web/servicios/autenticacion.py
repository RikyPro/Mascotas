import requests

from web.servicios import rest_api


def validar_credenciales(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def borrar_usuario(ID):
    body = {"id": ID}
    respuesta = requests.delete(f'{rest_api.API_URL}/usuarios{ID}', json=body)
    return respuesta.status_code == 200

def modificar_usuario(usuario, clave, rol, id):
    body = {"nombre": usuario,
            "clave": clave,
            "rol": rol,
            "id": id}
    respuesta = requests.put(f'{rest_api.API_URL}/usuarios{id}', json=body)
    return respuesta.status_code == 200