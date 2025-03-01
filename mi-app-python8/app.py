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

@app.route('/')
def hello():
    # Esta función retorna un mensaje simple de texto cuando se accede a la ruta "/"
    return "!Hola desde un contenedor Docker con Python y Flask!"

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

@app.route('/students', methods=['PATCH'])
def patch_student():
    # Obtener los datos del estudiante desde la solicitud JSON
    updated_fields = request.get_json()

    # Verificar que el id esté presente en la solicitud
    if 'id' not in updated_fields:
        return jsonify({"error": "Debe proporcionar el id del estudiante"}), 400  # 400: Solicitud incorrecta

    # Buscar al estudiante con el ID proporcionado en la base de datos
    student_to_update = Student.query.get(updated_fields['id'])

    if not student_to_update:
        # Si no se encuentra el estudiante, devolver un error
        return jsonify({"error": "Estudiante no encontrado"}), 404  # 404: No encontrado

    # Si solo se proporciona el id y no otros campos, no se actualiza nada
    if len(updated_fields) == 1 and 'id' in updated_fields:
        return jsonify({"message": "No se actualizó nada. Solo se proporcionó el ID."}), 400  # 400: Solicitud incorrecta

    # Actualizar solo los campos que están presentes en la solicitud
    if 'nombre' in updated_fields:
        student_to_update.nombre = updated_fields['nombre']
    if 'edad' in updated_fields:
        student_to_update.edad = updated_fields['edad']
    if 'carrera' in updated_fields:
        student_to_update.carrera = updated_fields['carrera']

    # Guardar los cambios en la base de datos
    db.session.commit()

    # Respuesta exitosa con los datos actualizados del estudiante
    return jsonify({
        "message": "Estudiante actualizado exitosamente",
        "student": {
            "id": student_to_update.id,
            "nombre": student_to_update.nombre,
            "edad": student_to_update.edad,
            "carrera": student_to_update.carrera
        }
    })

# Crear las tablas en la base de datos si no existen
with app.app_context():
    db.create_all()  # Crear las tabla

# Verificamos si el archivo está siendo ejecutado como el script principal.
# Si es así, iniciamos la aplicación Flask.
if __name__ == '__main__':
    # `app.run()` ejecuta el servidor de desarrollo de Flask en el puerto 5000,
    # y `host='0.0.0.0'` hace que la aplicación sea accesible desde cualquier dirección IP
    # (lo que es necesario cuando se ejecuta dentro de un contenedor Docker).
    app.run(host='0.0.0.0', port=5000)  