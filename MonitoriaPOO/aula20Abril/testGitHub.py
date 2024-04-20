def soma(a, b):
    return a + b






def ola(pessoa):
    resultado = f'Ola, {pessoa}'
    return(resultado)

###Pate principal do codigo 
def main():
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))

    
    resultado = soma(num1,num2)
    
    print(f'{num1} + {num2} = {resultado}')
    

y = ola('Maicon')    
x = soma(1,3)
resultado = x + 3
resultado2 = y + '. Como vai?'
ola('Iyryan')
main()