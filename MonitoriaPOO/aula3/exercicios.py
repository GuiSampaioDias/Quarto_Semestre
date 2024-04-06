##Exercicio 1
dic = {}
while len(dic):
    print('1- Para cadastrar: \n 2- Para exibir: \n3 Para encerrar: ')
    valor_usuario = input('Digite a sua opção: ')

    if valor_usuario == '1':
        nome = input("Digite o Nome: ")
        while True:
            cpf = input("CPF (apenas os números): ")
            if len(cpf) == 11:
                cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
                break
            else:
                print('Cpf inválido')
        dic[cpf] = nome
    elif valor_usuario == '2':
        if len(dic) == 0:
            print('\nNenhuma pessoa cadastrada\n')
        else:
            print(dic)

    elif valor_usuario =='3':
        print('\n Programa encerrado\n')
        break
    
    else:
        print('\n')
        print('Valor inválido\n')

##Exercício 2


