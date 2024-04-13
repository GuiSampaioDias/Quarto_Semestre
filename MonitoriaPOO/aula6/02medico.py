"""
Classe Paciente
Atributos:
- nome
- cpf
- idade
Métodos:
- não possui
Classe Medico
Atributos:
- nome
- crm
- especializacao
Métodos:
- não possui

Classe Exame
Atributos:
- medico: objeto da classe Medico
- paciente: objeto da classe Paciente
- descricao
- resultado
Métodos:
- imprimir_exame(): exibe um relatório com os dados do exame (inclusive os dados
do médico e do paciente)

Você pode utilizar o programa a seguir para testar as suas classes:
paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)
"""
class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao 

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        resultado = f'''
Paciente: {self.paciente.nome}             Médico: {self.medico.nome}  
CPF:      {self.paciente.cpf}              CRM:    {self.medico.crm}
\nRealizado o teste de {self.descricao}\nResultado: {self.resultado}
'''
        print(resultado)

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)


  #imprimir_exame(): exibe um relatório com os dados do exame (inclusive os dadosdo médico e do paciente)      