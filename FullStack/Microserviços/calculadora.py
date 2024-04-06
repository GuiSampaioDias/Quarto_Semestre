import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
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
    

class Testes(TestCase):
    def tet_soma(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(55,10,'soma'), 65)

    def test_divisao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(10, 5, 'divisao'), 2)

    def test_multiplicacao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(100, 10, 'MultiPlicacao'), 1000)

    def test_subtracao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(250, 200, 'Subtracao'),50)
    
        
        

class Main(object):
    calculator = Calculadora()
    resultado = calculator.calcular(25, 13, 'soma')
    print(resultado)    

if __name__ == "__main__":
    main()