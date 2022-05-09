import os.path

from flask import Flask, request, redirect, url_for, send_from_directory
from flask import render_template
from web.servicios import autenticacion

app = Flask(__name__)

UPLOAD_FOLDER = os.path.abspath("./uploads")
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)



@app.route('/inicio')
def inicio():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios)

@app.route('/veterinarias')
def veterinarias():
    return render_template('veterinarias.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        f = request.files["ourfile"]
        filename = f.filename
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for('get_file', filename=filename))

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

@app.route('/refugios')
def refugios():
    return render_template('refugios.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/donaciones')
def donaciones():
    return render_template('donaciones.html')

@app.route('/terminos')
def terminos():
    return render_template('terminos.html')


@app.route('/borrado', methods=['GET', 'POST'])
def borrado():
    error = None
    if request.method == 'POST':
        if not autenticacion.borrar_usuario(request.form['ID']):
            error = 'No se pudo eliminar el usuario'
        else:
            error = 'Se precedió a la eliminación del usuario'
    return render_template('borrado.html', error=error)


@app.route('/modificado', methods=['GET', 'POST'])
def modificado():
    error = None
    if request.method == 'POST':
        if not autenticacion.modificar_usuario(request.form['login'], request.form['password'], request.form['rol'], request.form['id']):
            error = 'No se pudo modificar el usuario'
        else:
            error = 'Usuario modificado correctamente'
    return render_template('modificado.html', error=error)

@app.route('/usuariosRegistrados')
def usuariosRegistrados():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
