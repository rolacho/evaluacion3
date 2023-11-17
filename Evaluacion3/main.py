from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PAGP.html')

@app.route('/EJERCICIO1', methods=['GET', 'POST'])
def EJERCICIO1():
    if request.method == 'POST':
        try:
            Nota1 = float(request.form['Nota1'])
            Nota2 = float(request.form['Nota2'])
            Nota3 = float(request.form['Nota3'])
            Asistencia = int(request.form['Asistencia'])
        except ValueError:
            return 'Error en los datos ingresados. Asegúrate de ingresar números válidos.'

        if not (1.0 <= Nota1 <= 7.0 and 1.0 <= Nota2 <= 7.0 and 1.0 <= Nota3 <= 7.0):
            return 'Error: Las notas deben estar en el rango [1, 7].'

        if not (0 <= Asistencia <= 100):
            return 'Error: La asistencia debe estar en el rango [0, 100].'

        total = Nota1 + Nota2 + Nota3
        promedio = total / 3

        mensaje = f'Promedio: {promedio}'

        if promedio < 4.0 or Asistencia < 75:
            mensaje += '<br>Resultado: Reprobado'
        elif promedio >= 4.0 and Asistencia >= 75:
            mensaje += '<br>Resultado: Aprobado'
        else:
            mensaje += '<br>Resultado: Datos incorrectos'

        return render_template('EJERCICIO1.html', resultado=mensaje)

    return render_template('EJERCICIO1.html')

@app.route('/EJERCICIO2', methods=['GET', 'POST'])
def EJERCICIO2():
    if request.method == 'POST':
        try:
            Nombre1 = request.form['Nombre1']
            Nombre2 = request.form['Nombre2']
            Nombre3 = request.form['Nombre3']

            # Eliminar espacios y encontrar el nombre más largo
            nombres_sin_espacios = [nombre.replace(" ", "") for nombre in [Nombre1, Nombre2, Nombre3]]
            nombre_mas_largo = max(nombres_sin_espacios, key=len)
            cantidad_letras_mas_largo = len(nombre_mas_largo)

            mensaje = f'El nombre más largo es: {nombre_mas_largo}, con {cantidad_letras_mas_largo} letras.'

            return render_template('EJERCICIO2.html', resultado=mensaje)
        except ValueError:
            return 'Error en los datos ingresados. Asegúrate de ingresar nombres válidos.'

    return render_template('EJERCICIO2.html')

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()