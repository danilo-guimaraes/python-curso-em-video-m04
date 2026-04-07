# Declaração de Classe
class Gafanhoto:
    def __init__(self):  # Método Construtor

        # Atributos de instancia
        self.nome = ""
        self.idade = 0

    # Metodo de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'


# Declaração de objeto
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = str(input('Nome: ').capitalize())
g3.idade = int(input('Idade: '))
g3.aniversario()
print(g3.mensagem())

g4 = Gafanhoto()
g4.nome = 'Marcos'
g4.idade = 23
print(g4.mensagem())
