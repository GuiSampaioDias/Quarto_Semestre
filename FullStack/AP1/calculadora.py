from flask import Flask, request, render_template

app = Flask(__name__)




#o calculadora aqui é o mesmo que esta na action do form no arquivo html, essa função só será usada quando a rota aula1 for ativada
@app.route('/calculadora',methods=['POST'])
def calcular():
    valor1 = request.form['valor1']
    valor2 = request.form['valor2']
    operacao = request.form['operacao']
    if valor1 == '' or valor2 == '':
        return render_template('calculadora.html', msg='Insira valores numerais nas caixas')
    if valor2 == '0' and operacao == 'divisao':
        return render_template('calculadora.html', msg='O denominador não pode ser = 0 na divisão')
    
    valor1 = float(valor1)
    valor2 = float(valor2) 

    if operacao == 'soma':
        resposta = valor1 + valor2
    elif operacao == 'divisao':
        resposta = valor1 / valor2
    elif operacao == 'multiplicacao':
        resposta =  valor1 * valor2
    elif operacao == 'subtracao':
        resposta = valor1 - valor2 
    resposta = str(resposta)

    print(valor1)
    return render_template('calculadora.html', msg=resposta)
    # Esse return vai renderizar o aul1 e fazer a resposta aparecer  embaixo dentro do <p>{{msg}}</p> do arquivo html

# o route aula1 renderiza tem como função chamar o arquivo 'aulamvc.html' que esta dentro da pasta templates. methodo get e post anbos obrigatorios
@app.route('/', methods=['POST', 'GET'])
def renderiza():
    return render_template('calculadora.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

