"""
Implemente as classes Produto e Pedido.
Classe Pedido:
Atributos:
- produtos: Lista de objetos do classe Produto (inicializar no construtor como uma
lista vazia)
Métodos:
- adicionar_produto: recebe um objeto Produto e o adiciona na lista de produtos.
- calcular_valor: deve retornar o valor total do pedido (somatório dos preços dos
produtos multiplicado pela quantidade de itens)

Classe Produto:
Atributos:
- nome: nome do produto
- preco: preço do produto
- quantidade: quantidade de itens do produto
Métodos:
- Não possui

Você pode utilizar o programa abaixo para testar as suas classes:
cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor()) # imprime 20.90
"""

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        valor_total_carrinho = 0
        for produto in self.produtos:
            valor_total_carrinho += (produto.preco * produto.quantidade)
        return valor_total_carrinho
    
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor()) # imprime 20.90