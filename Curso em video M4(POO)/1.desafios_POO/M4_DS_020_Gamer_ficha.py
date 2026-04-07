from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def __str__(self):
        return f'{self.nome} - {self.nick}'

    def add_favoritos(self,game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)


    def ficha(self):
        conteudo = f'Nome real: {self.nome}'
        conteudo += f'\nJogos favoritos:\n'
        for num, game in enumerate(self.favoritos):
            conteudo += f'[purple]:video_game:[/] {game}\n'
        painel = Panel(conteudo, title=f'Jogador {self.nick}',width=40)
        print(painel)

j1 = Gamer('Danilo', 'Bronks')
j1.add_favoritos('Fortnite')
j1.add_favoritos('CS2')
j1.add_favoritos('Valorant')
j1.ficha()

j2 = Gamer('Esthefany', 'Tefa')
j2.add_favoritos('Valorant')
j2.ficha()

