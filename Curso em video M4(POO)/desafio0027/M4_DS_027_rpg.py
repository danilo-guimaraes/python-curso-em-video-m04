from random import randint, randrange
from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod



class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100 ):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f'[red]{self.nome}[/][blue] atacou[/] {alvo.nome}[blue] com um[/blue] {golpe} [blue]de [red]'
                  f'{forca}[/] de '
                  f'Dano[/]\n')
            alvo.receber_dano(forca)

        else:
            print(f'[blue]O ataque de [white]{self.nome}[/] -> [white]{alvo.nome}[/] nao pode acontecer pois'
                  f' [white]{alvo.nome}[/] tem '
                  f'[red]({self.vida}HP), [white]{alvo.nome}[/] esta morto[/]\n')

    def receber_dano(self, dano):
        fator = randint(0,dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} [blue]recebeu dano de [red]{fator}[/] lhe sobrou [red]({self.vida})[/] de HP\n')

    @abstractmethod
    def curar(self):
        pass

    def status(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'facada', 'slash']

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f'[gree]{self.nome}[/] [blue]usou (potion) e recuperou [green]{fator}[/] de HP[/blue]\n ')

    def status(self):
        painel = Panel(f'Nick: {self.nome}\n'
                       f'HP: {self.vida}\n'
                       f'Magias: {self.golpes}', title=f'STATUS DE {self.nome}')
        print(painel)


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Evil Spirit', 'Aqua beam hall', 'fire']

    def curar(self):
        fator = randint(-50, 50)
        self.vida += fator
        if fator > 0:
            print(f'[gree]{self.nome}[/] [blue]usou (POTION) e recuperou [green]{fator}[/] de HP[/blue]\n ')

        else:
            print(f'{self.nome} [blue]esta sem[/] [red](POTION)[/]')

    def status(self):
        painel = Panel(f'Nick: {self.nome}\n'
                       f'HP: {self.vida}\n'
                       f'Magias: {self.golpes}'
                       , title=f'STATUS DE {self.nome}')
        print(painel)
