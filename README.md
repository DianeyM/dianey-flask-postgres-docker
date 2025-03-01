# Proyecto Flask Dockerizado con PostgreSQL

### CLARIDAD CLAVE: 
Existen dos versiones de este proyecto: **mi-app-python6** y **mi-app-python8**. La versión estable es **mi-app-python8**, ya que **mi-app-python6** presenta un problema en el archivo `app.py`, ya que no incluye el código que activa la creación de la tabla `Students`.

Este es un proyecto que implementa una **API en Python-Flask**, la cual interactúa con una base de datos **PostgreSQL**. El proyecto está **dockerizado** para facilitar su despliegue y ejecución en cualquier entorno.

---

### Requisitos

- Docker
- Docker Compose
- Python 3.9 o superior

---

### Estructura del Proyecto

- **`app.py`**: Código principal de la API en Flask.
- **`config.py`**: Configuración para la conexión con PostgreSQL.
- **`docker-compose.yml`**: Configuración de Docker Compose para los contenedores de la app y la base de datos.
- **`Dockerfile`**: Dockerfile para crear la imagen del contenedor de la app.
- **`init_db.py`**: Inicialización de la base de datos con Flask-SQLAlchemy.
- **`requirements.txt`**: Dependencias necesarias para la app.

---

### Instrucciones para correr el proyecto

1. **Clona el repositorio**

   Primero, clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/DianeyM/dianey-flask-postgres-docker
