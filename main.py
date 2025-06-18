from flask import Flask, render_template
from flask import request

app = Flask(__name__)
estudiantes_lista = []
@app.route('/', methods=['GET', 'POST'])
def estudiantes():

    if request.method == 'POST':
        nombre = request.form.get('est_nombre')
        carrera = request.form.get('est_carrera')
        e = {
            'nombre': nombre,
            'carrera': carrera
        }
        estudiantes_lista.append(e)
    return render_template('estudiantes.html', est = estudiantes_lista)


if __name__ == '__main__':
    app.run()