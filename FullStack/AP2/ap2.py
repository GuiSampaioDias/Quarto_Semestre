'''
create schema Ap2;

use Ap2;

CREATE TABLE tbl_pessoa (
      id_pessoa BIGINT NOT NULL AUTO_INCREMENT, 
      Nome VARCHAR(45) NULL, 
      Sobrenome VARCHAR(45) NULL, 
      Cor VARCHAR(45) NULL, 
      
      PRIMARY KEY (id_pessoa));

'''





import os
from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'Ap2'
app.config['MYSQL_DATABASE_HOST'] = 'db'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
mysql.init_app(app)




@app.route('/')
def telaInicial():
    return render_template('cadastrar.html')

@app.route('/form_cadastrar',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _sobrenome = request.form['inputSobrenome']
        _cor = request.form['inputCor']

        # validate the received values
        if _name and _sobrenome and _cor:

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('insert into tbl_pessoa (Nome, Sobrenome, Cor) VALUES (%s, %s, %s)', ( _name,_sobrenome,_cor))
            conn.commit()
            msg = "Cadastro realizado com sucesso"
            return render_template('cadastrar.html', msg = msg)
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/list',methods=['POST','GET'])
def listar():
    try:
            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select * from tbl_pessoa') 
            data = cursor.fetchall()
            print(data[0])
            msg = "Nenhuma Registro até o momento"
            print('Abaixo')
            print(data)
            print(type(data))
            if len(data) > 0:
                for x in range(len(data)):
                    print(data[x])
                    conn.commit()
                return render_template('listar_pessoas.html', datas=data)
            else:
                return render_template('listar_pessoas.html', msg = msg)
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        #cursor.close() 
        #conn.close()
        print ('oi')





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

