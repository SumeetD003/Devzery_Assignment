from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sdollars$'
app.config['MYSQL_DB'] = 'user_registration_db'




@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User registered successfully'})

@app.route('/users', methods=['GET'])

def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username, email FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

try:
    mysql = MySQL(app)
except Exception as e:
    print("Error connecting to MySQL:", e)
    
if __name__ == '__main__':
    app.run(debug=True)

CORS(app)