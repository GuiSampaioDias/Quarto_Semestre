import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(valor1, valor2, operador):
        operacaoFabrica = Operacao()
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
    @abstract
    def criar(self, valor1, valor2):
        pass
class Soma():
    def criar(self, valor1, valor2):
        return valor1 + valor2

        
        
        