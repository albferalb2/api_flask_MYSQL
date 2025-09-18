🐍 Flask REST API con MySQL

Este proyecto es una API REST construida con Flask que permite gestionar usuarios conectándose a una base de datos MySQL.

🚀 Funcionalidades

GET / → ruta principal de prueba

GET /users → lista todos los IDs de usuarios

GET /users/<id> → obtiene la información de un usuario específico

POST /users → crea un nuevo usuario en la base de datos

DELETE /users/<id> → elimina un usuario por su ID

🛠 Tecnologías utilizadas

Python 3

Flask

MySQL

mysql-connector-python

📦 Instalación

1. Clonar el repositorio

2. Instalar dependencias:

pip install flask mysql-connector-python


3. Configurar la base de datos en main.py:

db_config = {
    "host": "localhost",
    "user": "tu_usuario_mysql",
    "password": "tu_password_mysql",
    "database": "mydb"
}


4. Ejecutar:

python main.py

📌 Notas
