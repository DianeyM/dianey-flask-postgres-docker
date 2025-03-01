# Importamos la clase Flask, jsonify y recuest desde el módulo flask e importar json
from flask import Flask, jsonify, request
from init_db import db, init_db # Importar la instancia db y la función init_db desde init_db.py
from config import Config 

# Creamos una instancia de la clase Flask. 
# Esta instancia es nuestra aplicación.
app = Flask(__name__)
app.config.from_object(Config)  # Cargar la configuración desde config.py, Config es una clase en config.py

# Inicializamos la base de datos
init_db(app)

# Definimos el Modelo de los estudiantes
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.String(50), nullable=False)

# Rutas de la aplicación

@app.route('/students', methods=['GET'])
def get_students():
    students = db.session.query(Student).all()
    return jsonify([{"id": student.id, "nombre": student.nombre, "edad": student.edad, "carrera": student.carrera} for student in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(id=data['id'], nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Estudiante creado exitosamente", "student": data}), 201

@app.route('/students', methods=['DELETE'])
def delete_student():
    data = request.get_json()
    student_to_delete = db.session.query(Student).filter_by(id=data['id']).first()
    if not student_to_delete:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    db.session.delete(student_to_delete)
    db.session.commit()
    return jsonify({"message": "Estudiante eliminado exitosamente"}), 200

# Verificamos si el archivo está siendo ejecutado como el script principal.
# Si es así, iniciamos la aplicación Flask.
if __name__ == '__main__':
    # `app.run()` ejecuta el servidor de desarrollo de Flask en el puerto 5000,
    # y `host='0.0.0.0'` hace que la aplicación sea accesible desde cualquier dirección IP
    # (lo que es necesario cuando se ejecuta dentro de un contenedor Docker).
    app.run(debug=True, host='0.0.0.0', port=5000)   