class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getSond(self):
        return "Som do animal"
    
    def getState(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca, cor):
        super().__init__(nome, idade)
        self.raca = raca
        self.cor = cor

    def getSond(self):
        return "AU AU"
    
    def getState(self):
        estado = super().getState()
        return f'{estado}\nRaça: {self.raca}\nCor: {self.cor}'    

def main():
    animal = Animal('Baleia', 12)

    print(animal.getSond())
    print(animal.getState())

    cachorro = Cachorro('Toby', 5, 'Podle', 'Caramelo')
    print(cachorro.getSond())
    print(cachorro.getState())

main()