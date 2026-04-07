# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um Gafanho, que é uma pessoa que tem nome e idade.
Para criar uma pessoa, use
variável = Gafanhoto (nome, idade)
    """

    def __init__(self, nome='vazio', idade=0):  # Método Construtor

        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Metodo de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):  # Metodo Duder
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de objeto
g1 = Gafanhoto('Maria', 17)
g1.aniversario()


print(g1.__dict__)
print(g1.__getstate__()) #personalizaveu
print(g1.__class__)
print(g1.__doc__)  # Dunder Attribute

