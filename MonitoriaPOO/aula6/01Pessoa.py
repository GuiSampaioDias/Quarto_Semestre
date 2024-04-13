"""
A associação entre classes ocorre quando uma classe possui atributos que são objetos de outra
classe. De acordo com esse conceito, observe o diagrama de classes abaixo, que representa uma
associação onde uma Pessoa possui um Carro.

Implemente as classes Pessoa e Carro.
Classe Pessoa:
Atributos:
- nome: nome da pessoa
- idade: idade da pessoa
- carro: objeto da classe Carro
Métodos:
- Não possui.

Classe Carro:
Atributos:
- marca: marca do carro
- modelo: modelo do carro
- placa: placa do carro
- ano: ano de fabricação do carro
Métodos:
- Não possui

Você pode utilizar o trecho de programa abaixo para testar as suas classes:
meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)
print('Nome: ', eu.nome) # João
print('Idade: ', eu.idade) # 25
print('Marca do carro: ', eu.carro.marca) # Volkswagen
print('Modelo do carro: ', eu.carro.modelo) # Gol
print('Placa do carro: ', eu.carro.placa) # AAA-1111
print('Ano do carro: ', eu.carro.ano) # 2015"""

class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = carro

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)
print('Nome: ', eu.nome) # João
print('Idade: ', eu.idade) # 25
print('Marca do carro: ', eu.carro.marca) # Volkswagen
print('Modelo do carro: ', eu.carro.modelo) # Gol
print('Placa do carro: ', eu.carro.placa) # AAA-1111
print('Ano do carro: ', eu.carro.ano) # 2015