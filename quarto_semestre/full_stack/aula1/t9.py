from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def aula1():

    primos = "Tudo vai dar certo, meus caros alunos!"

    return primos
@app.route('/calc')
def calculadora():
    valor1 = request.args.get('v1')
    valor2 = request.args.get('v2')
    operacao = request.args.get('operacao')
    valor1 = int(valor1)
    valor2 = int(valor2)

    if operacao == 'soma':
        return str(valor1 + valor2)
    
    elif operacao == 'divisao':
        return str(valor1 / valor2)
    
    elif operacao == 'subtracao':
        return str(valor1 - valor2)
    
    elif operacao == 'multiplicacao':
        return str(valor1 * valor2)
    elif operacao == 'melhortime':
        return 'Vai Corinthians'
    else:
        return 'Operação inválida'
@app.route('/calcula', methods=['POST'])
def calcula():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['operacao']
    valor1 = int(valor1)
    valor2 = int(valor2)

    if operacao == 'soma':
        resp = (valor1 + valor2)
    
    elif operacao == 'divisao':
        resp = str(valor1 / valor2)
    
    elif operacao == 'subtracao':
        resp = str(valor1 - valor2)
    
    elif operacao == 'multiplicacao':
        resp = str(valor1 * valor2)
    
    else:
        resp = 'Operação inválida'
    return render_template('formulario.html', msg=resp)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name = name)
    

@app.route('/aula1', methods=['GET', 'POST'])
def renderiza():
    return render_template('formulario.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002,debug = True)

