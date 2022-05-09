from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion
from flask import render_template

app = Flask(__name__)

app.route('/')
def get_index():
    titulo_mascotas = 'Tu Mascota!!'
    return render_template('login.html', titulo=titulo_mascotas)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        autenticacion.crear_usuario(datos_usuario['nombre'], datos_usuario['clave'])
    except Exception:
        return 'El usuario ya existe', 412
    return 'OK', 200

@app.route('/usuarios<id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.modificar_usuario(id_usuario, datos_usuario)
    return 'OK', 200

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())

@app.route('/usuarios<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = autenticacion.obtener_usuario(id_usuario)
        return jsonify(usuario)
    except autenticacion.UserNotFound:
        return 'Usuario no encontrado', 404

@app.route('/usuarios<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    autenticacion.borrar_usuario(id_usuario)
    return 'Borrado', 200

@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        id_sesion = autenticacion.login(datos_usuario['nombre'], datos_usuario['clave'])
        return jsonify({"id_sesion": id_sesion})
    except autenticacion.UserNotFound:
        return 'USUARIO NO ENCONTRADO', 404

"""
@app.route('/mascotas', methods=['POST'])
def crear_mascota():
    datos_mascota = request.get_json()
    autenticacion.crear_mascota(datos_mascota['nombre'], datos_mascota['tipoanimal'], datos_mascota['foto'])
    return 'OK', 200

@app.route('/mascotas', methods=['PUT'])
def modificar_mascota():
    datos_mascota = request.get_json()
    autenticacion.modificar_mascota(datos_mascota['nombre'], datos_mascota['tipoanimal'], datos_mascota['foto'])
    return 'OK', 200

@app.route('/mascotas', methods=['GET'])
def leer_mascota():
    datos_mascota = request.get_json()
    autenticacion.leer_mascota(datos_mascota['nombre'], datos_mascota['tipoanimal'], datos_mascota['foto'])
    return 'OK', 200

@app.route('/mascotas', methods=['DELETE'])
def eliminar_mascota():
    datos_mascota = request.get_json()
    autenticacion.eliminar_mascota(datos_mascota['nombre'], datos_mascota['tipoanimal'], datos_mascota['foto'])
    return 'OK', 200

@app.route('/veterinarias', methods=['POST'])
def crear_veterinaria():
    datos_veterinaria = request.get_json()
    autenticacion.crear_veterinaria(datos_veterinaria['nombre'], datos_veterinaria['ubicacion'], datos_veterinaria['servicios'])
    return 'OK', 200

@app.route('/veterinarias', methods=['PUT'])
def modificar_veterinaria():
    datos_veterinaria = request.get_json()
    autenticacion.modificar_veterinaria(datos_veterinaria['nombre'], datos_veterinaria['ubicacion'], datos_veterinaria['servicios'])
    return 'OK', 200

@app.route('/veterinarias', methods=['GET'])
def leer_veterinaria():
    datos_veterinaria = request.get_json()
    autenticacion.leer_veterinaria(datos_veterinaria['nombre'], datos_veterinaria['ubicacion'], datos_veterinaria['servicios'])
    return 'OK', 200

@app.route('/veterinarias', methods=['DELETE'])
def eliminar_veterinaria():
    datos_veterinaria = request.get_json()
    autenticacion.eliminar_veterinaria(datos_veterinaria['nombre'], datos_veterinaria['ubicacion'], datos_veterinaria['servicios'])
    return 'OK', 200

@app.route('/refugios', methods=['POST'])
def crear_refugio():
    datos_refugio = request.get_json()
    autenticacion.crear_refugio(datos_refugio['nombre'], datos_refugio['ubicacion'], datos_refugio['mascotasenadopcion'])
    return 'OK', 200

@app.route('/refugios', methods=['PUT'])
def modificar_refugio():
    datos_refugio = request.get_json()
    autenticacion.modificar_refugio(datos_refugio['nombre'], datos_refugio['ubicacion'], datos_refugio['mascotasenadopcion'])
    return 'OK', 200

@app.route('/refugios', methods=['GET'])
def leer_refugio():
    datos_refugio = request.get_json()
    autenticacion.leer_refugio(datos_refugio['nombre'], datos_refugio['ubicacion'], datos_refugio['mascotasenadopcion'])
    return 'OK', 200

@app.route('/refugios', methods=['DELETE'])
def eliminar_refugio():
    datos_refugio = request.get_json()
    autenticacion.eliminar_refugio(datos_refugio['nombre'], datos_refugio['ubicacion'], datos_refugio['mascotasenadopcion'])
    return 'OK', 200
"""

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)

