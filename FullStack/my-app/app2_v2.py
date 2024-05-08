import os 
from flask import Flask, render_template, json, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'impacta2024'
app.config['MYSQL_DB'] = 'teste'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route('/api/say_name5', methods=['GET','POST'])
def say_name5():
    json = request.get_json()
    nome = json['txtNome']
    print(nome)

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute('insert into Ap2 (nome) VALUES (%s)', (nome,))
    conn.commit()
    return jsonify(first_name=nome)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)