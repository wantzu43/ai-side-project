# simple flask app that connects to mysql and returns data
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        port=3306,
        user="flask_user",
        password="flask_password",
        database="flask_db"
    )

@app.route("/data")
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except mysql.connector.Error as err:
        return f"Database error: {err}", 500

@app.route('/users')
def get_users():
    return "This is the users endpoint"

@app.route("/")
def index():
    return "Hello from Flask + MySQL + Copilot!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
