from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de la base de datos
db = SQLAlchemy()

# Inicializar SQLAlchemy en una aplicación Flask. 
def init_db(app):
    db.init_app(app)