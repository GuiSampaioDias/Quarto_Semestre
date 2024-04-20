def valor_compra(valores, quantidade, nome):
    total = 0
    for i in range(len(valores)):
        total_por_produto = 0
        total_por_produto += valores[i] * quantidade[i]
        total += valores[i] * quantidade[i]
        print(f'{nome[i]}: {quantidade[i]} x {valores[i]} = {total_por_produto}')
    return(f'Valor total da compra para sair com a gata {total}')


def main():
    nome = ['camisinha', 'Suco de uva integral', 'salgadinho' ]
    quantidade = [2, 1, 2]
    valores = [10, 20, 5]
    print(valor_compra(valores, quantidade, nome))
    return 'Fim'

y = 10
x = 'Banana'
print(f'{x} amassada com aveia')
print(f'resultado: {main()}')
