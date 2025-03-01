import os #Importamos la librería os para acceder a variables de entorno.

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Estás desactivando para reducir el uso de memoria y mejorar el rendimiento.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/students_db') # Se le indica a Flask-SQLAlchemy cómo conectarse a la db, indicandole la URL de la db.