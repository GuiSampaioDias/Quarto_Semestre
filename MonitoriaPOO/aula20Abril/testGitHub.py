def soma(a, b):
    return a + b

def ola(pessoa):
    resultado = f'Ola, {pessoa}'
    print(resultado)

###Pate principal do codigo 
def main():
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))

    
    resultado = soma(num1,num2)
    
    print(f'{num1} + {num2} = {resultado}')
    

ola('Maicon')    
print(soma(1,3))
main()