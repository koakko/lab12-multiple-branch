from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_PATH = "database.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                industry TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/register', methods=['POST'])
def register_company():
    data = request.json
    name = data['name']
    email = data['email']
    industry = data['industry']

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO companies (name, email, industry) VALUES (?, ?, ?)",
                  (name, email, industry))
        conn.commit()
    return jsonify({'message': 'Company registered successfully'}), 201

@app.route('/companies', methods=['GET'])
def get_companies():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id, name, email, industry FROM companies")
        companies = [dict(zip(['id', 'name', 'email', 'industry'], row)) for row in c.fetchall()]
    return jsonify(companies)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
