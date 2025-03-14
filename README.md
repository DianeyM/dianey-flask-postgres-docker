# Proyecto Flask Dockerizado con PostgreSQL

**CLARIDAD CLAVE**: 
Hay dos versiones de este proyecto: mi-app-python6 y mi-app-python8. La **versión estable es mi-app-python8**. mi-app-python6 tiene un problema en el archivo app.py porque no tiene el código que activa la creación de la tabla Students. 

Este es un proyecto que implementa una API en **Python-Flask**, la cual interactúa con una base de datos **PostgreSQL**. El proyecto está dockerizado para facilitar su despliegue y ejecución en cualquier entorno.

## Requisitos

- Docker.
- Docker Compose.
- Python 3.9 o superior.

## Estructura del Proyecto

- app.py               # Código principal de la API en Flask
- config.py            # Configuración para la conexión con PostgreSQL.
- docker-compose.yml   # Configuración de Docker Compose para los contenedores de la app y la base de datos.
- Dockerfile           # Dockerfile para crear la imagen del contenedor de la app.
- init_db.py           # Inicialización de la base de datos con Flask-SQLAlchemy.
- requirements.txt     # Dependencias necesarias para la app

## Instrucciones para correr el proyecto

### 1. Clona el repositorio

Primero, clona el repositorio en tu máquina local:

    git clone https://github.com/DianeyM/dianey-flask-postgres-docker

### 2. Construir y ejecutar los contenedores con Docker Compose

Este proyecto utiliza **Docker** y **Docker Compose** para orquestar la app y la base de datos. Puedes construir y ejecutar los contenedores con el siguiente comando, estando en el interior de la carpeta clonada:

     docker-compose up --build

Este comando realizará lo siguiente:

- Construirá la imagen de la aplicación web usando el archivo `Dockerfile`.
- Descargar e inicializará la imagen de PostgreSQL.
- Ejecutará ambos contenedores (la aplicación y la base de datos) con los puertos configurados.

Luego se puede precional control + C y: 

     docker-compose up -d

### 3. Acceder a la API

Una vez que los contenedores estén en ejecución, la API estará disponible en:

    http://localhost:5006

Puedes acceder a los siguientes endpoints de la API:

- **GET /**: Mostrar un mensaje: !Hola desde un contenedor Docker con Python y Flask!.
- **GET /students**: Obtener la lista de todos los estudiantes.
- **POST /students**: Crear un nuevo estudiante.
- **DELETE /students**: Eliminar un estudiante por su ID y NOMBRE.
- **PATCH /students**: Actualizar la información de un estudiante.

Se pueden ejecutar los siguientes comandos para probar la funcionalidad completa de la aplicación multicontenedor: 

**3.1.Ver el mensaje !Hola desde un contenedor Docker con Python y Flask!**:
- curl localhost:5006/
  
**3.2.Ver los estudiantes en la Base de Datos. Que en un inicio está vacia:**:
- curl localhost:5006/students
  
**3.3.Alimentar la base de datos con tres estudiantes:**:
- curl -X POST http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 1, "nombre": "Dianey Macias", "edad": 30, "carrera": "Ing. Sistemas"}'
- curl -X POST http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 2, "nombre": "Ana Gomez R", "edad": 21, "carrera": "Matematicas"}'
- curl -X POST http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 3, "nombre": "Luis", "edad": 23, "carrera": "Fisica"}'
  
**3.4.Actualizar algunos datos de un estudiante:**:
- curl -X PATCH http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 3, "edad": 25}'
- curl -X PATCH http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 3, "nombre": "Luis Roa", "carrera": "Fisica cuantica"}'
- curl -X PATCH http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 3}'

**3.5.Eliminar un estudiante:**:
- curl -X DELETE http://localhost:5006/students -H "Content-Type: application/json" -d '{"id": 3, "nombre": "Luis Roa"}'

**3.6.Ver los estudiantes en la Base de Datos:**:
- curl localhost:5006/students

### 4. Ver los logs de los contenedores

Puedes ver los logs de los contenedores con el siguiente comando:

    docker-compose logs -f

Este comando te permitirá ver la salida de los logs tanto de la app como de la base de datos.

### 5. Detener los contenedores

Para detener y eliminar los contenedores, puedes ejecutar:

    docker-compose down       

Este comando detendrá y eliminará los contenedores, pero los datos de PostgreSQL se mantendrán persistentes gracias al volumen configurado.

## Estructura de la base de datos

El proyecto tiene una tabla `students` que almacena la siguiente información:

- **id**: Identificador único del estudiante (auto-incremental).
- **nombre**: Nombre del estudiante.
- **edad**: Edad del estudiante.
- **carrera**: Carrera que cursa el estudiante.

## Variables de Entorno

La aplicación usa las siguientes variables de entorno:

- **FLASK_ENV**: Configura el entorno de Flask. En desarrollo, se recomienda configurarlo como `development`.
- **DATABASE_URL**: La URL de conexión a la base de datos PostgreSQL. Esta se configura automáticamente a través de Docker Compose.

## Dependencias

Las dependencias necesarias para la aplicación están listadas en el archivo `requirements.txt`:

- `Flask`: El framework web para construir la API.
- `psycopg2-binary`: Adaptador PostgreSQL para Python.
- `Flask-SQLAlchemy`: Extensión de Flask para trabajar con bases de datos SQL.
- `Werkzeug`: Biblioteca que soporta funcionalidades como manejo de errores, entre otras.

## Problemas comunes

### Error de conexión a la base de datos

Si la aplicación no puede conectarse a la base de datos, asegúrate de que Docker esté ejecutando ambos contenedores y que no haya problemas con la red de Docker.

### Cambios en el código

Si realizas cambios en el código, es posible que necesites reconstruir los contenedores:

    ```docker-compose up --build

### Localhost si se usa una máquina virtual y se dokeriza en el interior de la misma:

Para acceder a los Endpoints desde la máquina física no use: - curl localhost:5006/students, en su lugar use: http://IP_DE_MÁQUINA_VIRTUAL:5006/students. Porque la IP de la máquina virtual es la que direcciona al docker.

Para tal fin, debe deteminar la ip de su máquina virual y haber instalado el sistema operativo de la máquina virtual en modo BRIDGE.
