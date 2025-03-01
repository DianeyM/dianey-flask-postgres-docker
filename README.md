<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Flask Dockerizado con PostgreSQL</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid #ddd;
        }
        code {
            font-family: "Courier New", Courier, monospace;
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        ol {
            margin-left: 20px;
        }
        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Proyecto Flask Dockerizado con PostgreSQL</h1>

    <p>Este es un proyecto que implementa una API en <strong>Python-Flask</strong> que interactúa con una base de datos <strong>PostgreSQL</strong>. El proyecto está dockerizado para facilitar su despliegue y ejecución en cualquier entorno.</p>

    <h2>Requisitos</h2>
    <ul>
        <li>Docker</li>
        <li>Docker Compose</li>
        <li>Python 3.9 o superior (si deseas correrlo sin Docker)</li>
    </ul>

    <h2>Estructura del Proyecto</h2>
    <pre>
.
├── app.py              # Código principal de la API en Flask
├── config.py           # Configuración para la conexión con PostgreSQL
├── docker-compose.yml  # Configuración de Docker Compose para los contenedores de la app y la base de datos
├── Dockerfile          # Dockerfile para crear la imagen del contenedor de la app
├── init_db.py          # Inicialización de la base de datos con Flask-SQLAlchemy
├── requirements.txt    # Dependencias necesarias para la app
    </pre>

    <h2>Instrucciones para correr el proyecto</h2>

    <h3>1. Clona el repositorio</h3>
    <p>Primero, clona el repositorio en tu máquina local:</p>
    <pre><code>git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio</code></pre>

    <h3>2. Construir y ejecutar los contenedores con Docker Compose</h3>
    <p>Este proyecto utiliza <strong>Docker</strong> y <strong>Docker Compose</strong> para orquestar la app y la base de datos. Puedes construir y ejecutar los contenedores con el siguiente comando:</p>
    <pre><code>docker-compose up --build</code></pre>
    <p>Este comando realizará lo siguiente:</p>
    <ul>
        <li>Construirá la imagen de la aplicación web usando el archivo <code>Dockerfile</code>.</li>
        <li>Descargar e inicializará la imagen de PostgreSQL.</li>
        <li>Ejecutará ambos contenedores (la aplicación y la base de datos) con los puertos configurados.</li>
    </ul>

    <h3>3. Acceder a la API</h3>
    <p>Una vez que los contenedores estén en ejecución, la API estará disponible en:</p>
    <pre><code>http://localhost:5006</code></pre>

    <p>Puedes acceder a los siguientes endpoints de la API:</p>
    <ul>
        <li><strong>GET /students</strong>: Obtener la lista de todos los estudiantes.</li>
        <li><strong>POST /students</strong>: Crear un nuevo estudiante.</li>
        <li><strong>DELETE /students</strong>: Eliminar un estudiante por su ID.</li>
        <li><strong>PATCH /students</strong>: Actualizar la información de un estudiante.</li>
    </ul>

    <h3>4. Ver los logs de los contenedores</h3>
    <p>Puedes ver los logs de los contenedores con el siguiente comando:</p>
    <pre><code>docker-compose logs -f</code></pre>
    <p>Este comando te permitirá ver la salida de los logs tanto de la app como de la base de datos.</p>

    <h3>5. Detener los contenedores</h3>
    <p>Para detener los contenedores, puedes ejecutar:</p>
    <pre><code>docker-compose down</code></pre>
    <p>Este comando detendrá y eliminará los contenedores, pero los datos de PostgreSQL se mantendrán persistentes gracias al volumen configurado.</p>

    <h2>Estructura de la base de datos</h2>
    <p>El proyecto tiene una tabla <code>students</code> que almacena la siguiente información:</p>
    <ul>
        <li><strong>id</strong>: Identificador único del estudiante (auto-incremental).</li>
        <li><strong>nombre</strong>: Nombre del estudiante.</li>
        <li><strong>edad</strong>: Edad del estudiante.</li>
        <li><strong>carrera</strong>: Carrera que cursa el estudiante.</li>
    </ul>

    <h2>Variables de Entorno</h2>
    <p>La aplicación usa las siguientes variables de entorno:</p>
    <ul>
        <li><strong>FLASK_ENV</strong>: Configura el entorno de Flask. En desarrollo, se recomienda configurarlo como <code>development</code>.</li>
        <li><strong>DATABASE_URL</strong>: La URL de conexión a la base de datos PostgreSQL. Esta se configura automáticamente a través de Docker Compose.</li>
    </ul>

    <h2>Dependencias</h2>
    <p>Las dependencias necesarias para la aplicación están listadas en el archivo <code>requirements.txt</code>:</p>
    <ul>
        <li><code>Flask</code>: El framework web para construir la API.</li>
        <li><code>psycopg2-binary</code>: Adaptador PostgreSQL para Python.</li>
        <li><code>Flask-SQLAlchemy</code>: Extensión de Flask para trabajar con bases de datos SQL.</li>
        <li><code>Werkzeug</code>: Biblioteca que soporta funcionalidades como manejo de errores, entre otras.</li>
    </ul>

    <h2>Problemas comunes</h2>

    <h3>Error de conexión a la base de datos</h3>
    <p>Si la aplicación no puede conectarse a la base de datos, asegúrate de que Docker esté ejecutando ambos contenedores y que no haya problemas con la red de Docker.</p>

    <h3>Cambios en el código</h3>
    <p>Si realizas cambios en el código, es posible que necesites reconstruir los contenedores:</p>
    <pre><code>docker-compose up --build</code></pre>
</body>
</html>
