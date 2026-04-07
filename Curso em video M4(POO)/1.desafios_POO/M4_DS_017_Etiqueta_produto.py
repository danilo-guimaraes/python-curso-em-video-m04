from rich import print
from rich.panel import Panel


class Produto:
    """
    Cria uma etiqueta personalizada para o produto
    """

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'

    def etiqueta(self):
        conteudo = f'[black]{self.nome.center(30, ' ')}[/]'
        conteudo += '=-' * 15
        precof = f'R${self.preco:,.2f}'
        conteudo += f'[black]{precof.center(30, '.')}[/]'
        etiqueta = Panel(conteudo, title='Produto', width=34, style='purple on white')
        print(etiqueta)
        print(f'{self.nome} custa R${self.preco:,.2f}')


p1 = Produto('Iphone 17 Pro Max', 9_000.34)
p2 = Produto('Notebook Gamer', 5_515.76)
p1.etiqueta()
p2.etiqueta()