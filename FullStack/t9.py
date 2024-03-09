from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def aula1():

    primos = "Tudo vai dar certo, meus caros alunos!"

    return primos


# Para o exemplo abaixo da rota calc, esse é um exemplo de rota que foi criada para testar o código na caixa do navegador 
#(http://localhost:5002/calc?v1=10&v2=5&operacao=soma ) aqui chamamos a rota calc passamos o valor da v1, v2 e a operação
@app.route('/calc')
def calculadora():
    valor1 = request.args.get('v1')
    valor2 = request.args.get('v2')
    operacao = request.args.get('operacao')
    valor1 = int(valor1)
    valor2 = int(valor2) 

    if operacao == 'soma':
        resposta = valor1 + valor2
    elif operacao == 'divisao':
        resposta = valor1 / valor2
    elif operacao == 'multiplicacao':
        resposta =  valor1 * valor2
    elif operacao == 'subtracao':
        resposta = valor1 - valor2 

    print(valor1)
    return str(resposta)


#o calcula aqui é o mesmo que esta na action do form no arquivo html, essa função só será usada quando a rota aula1 for ativada
@app.route('/calcula',methods=['POST'])
def calcula():
    valor1 = request.form['valor1']
    valor2 = request.form['valor2']
    operacao = request.form['operacao']
    valor1 = int(valor1)
    valor2 = int(valor2) 

    if operacao == 'soma':
        resposta = valor1 + valor2
    elif operacao == 'divisao':
        resposta = valor1 / valor2
    elif operacao == 'multiplicacao':
        resposta =  valor1 * valor2
    elif operacao == 'subtracao':
        resposta = valor1 - valor2 

    print(valor1)
    return render_template('aulamvc.html', msg=resposta)
    # Esse return vai renderizar o aul1 e fazer a resposta aparecer  embaixo dentro do <p>{{msg}}</p> do arquivo html

# o route aula1 renderiza tem como função chamar o arquivo 'aulamvc.html' que esta dentro da pasta templates. methodo get e post anbos obrigatorios
@app.route('/aula1', methods=['POST', 'GET'])
def renderiza():
    return render_template('aulamvc.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

