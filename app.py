from flask import Flask, render_template, request
from connection import app, mysql  # Importar la instancia de la aplicación y MySQL desde connection.py
from crud_operations import crud_operations_blueprint

# Registrar el Blueprint con la aplicación principal
app.register_blueprint(crud_operations_blueprint)

# Resto del código de configuración y rutas en app.py

def interes_compuesto(capital, tasa, tiempo):
    monto_final = capital * (1 + tasa/100) ** tiempo
    monto_final = round(monto_final, 2)  # Redondear el resultado a dos decimales
    return monto_final

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        capital = float(request.form['capital'])
        tasa = float(request.form['tasa'])
        tiempo = float(request.form['tiempo'])

        monto_final = interes_compuesto(capital, tasa, tiempo)

        # Store the data in the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO intcompuesto (capital, tasa, tiempo, monto_final) VALUES (%s, %s, %s, %s)",
                    (capital, tasa, tiempo, monto_final))
        mysql.connection.commit()
        cur.close()

        return render_template('index.html', capital=capital, tasa=tasa, tiempo=tiempo, monto_final=monto_final)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
