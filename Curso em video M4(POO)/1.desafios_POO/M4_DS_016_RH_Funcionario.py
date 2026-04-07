from click import style
from rich import print
from rich.panel import Panel
class funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.set = setor
        self.carg = cargo
        pass

    def apresentacao(self):
        print(f'[bold white]Ola, sou [cyan]{self.nome}[/] e sou [cyan]{self.carg}[/] de [cyan]{self.set}[/] da empresa Curso em video[/]')
        print()

    def aposentadoria(self):
        resp = str(input('Voce gostaria de se aposentar? (S/N) ')).strip()[0].upper()
        if resp == 'S':
            print(f'[green on black]{self.nome} Aposentado com sucesso no cargo de {self.carg}[/]:money-mouth_face:')
            print()
        else:
            print(f'[on black]Ate logo[/] [bold green]{self.nome}, volte sempre[/]:waving_hand:')
            print()


c1 = funcionario('Maria', 'Administração', 'Diretora')
c2 = funcionario('Danilo', 'TI', 'Desenvolvedor')

c1.apresentacao()
c1.aposentadoria()
c2.apresentacao()
c2.aposentadoria()

