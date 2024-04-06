import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if operador.upper() == 'SOMA':
            return Soma()
        elif operador.upper() == 'SUBTRACAO':
            return Subtracao()
        elif operador.upper() == 'MULTIPLICACAO':
            return Multiplicacao()
        elif operador.upper() == 'DIVISAO':
            return Divisao()
        
class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
    
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado
    
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado
    
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
    
teste1 = Calculadora.calcular(1,2,'SOMA')
print(teste1)
    

        
        
        