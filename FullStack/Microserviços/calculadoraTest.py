import abc
from unittest import TestCase, main


class Calculadora(object):
    def calcular(self, valor1, valor2, operacao):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operacao)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operacao):
        if operacao.lower() == 'soma':
            return Soma()
    
    def criar(self, operacao):
        if operacao.lower() == 'divisao':
            return Divisao()
    
    def criar(self, operacao):
        if operacao.lower() == 'subtracao':
            return Subtracao()
    
    def criar(self, operacao):
        if operacao.lower() == 'multiplicacao':
            return Multiplicacao()
    
        
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
    def test_soma(self):
        calculator = Calculadora()
        self.assertEqual(calculator.cria_soma(25, 13), 38)

    def test_divisao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(10, 5, 'divisao'), 2)

    def test_multiplicacao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(100, 10, 'MultiPlicacao'), 1000)

    def test_subtracao(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(250, 200, 'Subtracao'),50)

    def test_vitoria(self):
        calculator = Calculadora()
        self.assertEqual(calculator.calcular(18, 300, 'vitoria'), 0)
    
        
        

class Main(object):
    calculator = Calculadora()
    resultado = calculator.calcular(25, 13, 'soma')
    print(resultado)    

if __name__ == "__main__":
    main()