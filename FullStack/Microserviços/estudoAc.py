import abc


class Pessoa(metaclass=abc.ABCMeta):
    def  __init__(self,nome, cpf):
        self.nome = nome
        self.cpf= cpf
    
    @abc.abstractmethod
    def apresenta(self):
        pass


class Vendedor(Pessoa):
    def __init__(self,nome,cpf,numero):
         super().__init__(nome,cpf)
         self.numero = numero

    def apresenta(self):
        return f'Ola meu nome é {self.nome} e meu número é o  {self.numero}'
    

pessoa2 = Vendedor("Ze mane", 68, 24)
pessoa = Vendedor("Danilo",123,8)
print(pessoa.apresenta())
print(pessoa2.apresenta())



"""
class Controle():
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def escolhe_canal(self, x):
        self.canal = x

ligamos = Controle(10, 8)
print()
print(ligamos.canal)
print(ligamos.volume)

ligamos.escolhe_canal(39)
print(ligamos.canal)

def soma(a,b):
    resultado = a + b
    return resultado

calcular = soma(10, 20)
print(f'soma = {calcular}')

"""
