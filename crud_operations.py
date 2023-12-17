from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import Blueprint
from flask import Blueprint

# Crear un Blueprint
crud_operations_blueprint = Blueprint('crud_operations', __name__)

app = Flask(__name__)
mysql = MySQL(app)


# Operación de Crear (CREATE)
@crud_operations_blueprint.route('/intcompuesto', methods=['POST'])
def crear_registro():
    if request.method == 'POST':
        data = request.get_json()
        capital = data['capital']
        tasa = data['tasa']
        tiempo = data['tiempo']
        monto_final = data['monto_final']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO intcompuesto (capital, tasa, tiempo, monto_final) VALUES (%s, %s, %s, %s)", (capital, tasa, tiempo, monto_final))
        mysql.connection.commit()
        cur.close()
        return jsonify({'mensaje': 'Registro creado satisfactoriamente'})


# Operación de Leer (READ)
@crud_operations_blueprint.route('/intcompuesto', methods=['GET'])
def leer_registros():
    
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM intcompuesto")
    if result > 0:
        registros = cur.fetchall()
        return jsonify(registros)
    else:
        return jsonify({'mensaje': 'No se encontraron registros'})


# Operación de Modificar (UPDATE)
@crud_operations_blueprint.route('/intcompuesto/<int:id>', methods=['PUT'])
def modificar_registro(id):
    if request.method == 'PUT':
        data = request.get_json()
        capital = data['capital']
        tasa = data['tasa']
        tiempo = data['tiempo']
        monto_final = data['monto_final']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE intcompuesto SET capital = %s, tasa = %s, tiempo = %s, monto_final = %s WHERE id = %s", (capital, tasa, tiempo, monto_final, id))
        mysql.connection.commit()
        cur.close()
        return jsonify({'mensaje': 'Registro actualizado satisfactoriamente'})


# Operación de Eliminar (DELETE)
@crud_operations_blueprint.route('/intcompuesto/<int:id>', methods=['DELETE'])
def eliminar_registro(id):
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM intcompuesto WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'mensaje': 'Registro eliminado satisfactoriamente'})

# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)