from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "mydb"
}

# Obtener conexión
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def root():
    return "root"

# Obtener un usuario por ID
@app.route("/users/<userid>", methods=["GET"])
def get_user(userid):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (userid,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    query = request.args.get("query")
    if query:
        user["query"] = query
    
    return jsonify(user), 200

# Crear usuario
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    userid = data.get("id")
    name = data.get("name", "unknown")
    telephone = data.get("telephone", "000000000")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (id, name, telephone) VALUES (%s, %s, %s)",
            (userid, name, telephone)
        )
        conn.commit()
    except mysql.connector.IntegrityError:
        return jsonify({"error": "User already exists"}), 400
    finally:
        cursor.close()
        conn.close()
    
    return jsonify({"status": "user created", "user": data}), 201

# Eliminar usuario
@app.route("/users/<userid>", methods=["DELETE"])
def delete_user(userid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (userid,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": f"user {userid} deleted"}), 200

# Listar todos los IDs
@app.route("/users", methods=["GET"])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return jsonify({"user_ids": ids}), 200

if __name__ == "__main__":
    app.run(debug=True)
