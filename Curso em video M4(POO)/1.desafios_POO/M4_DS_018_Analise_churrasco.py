from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quant = quantidade

    def __str__(self):
        return f'Analisando {self.titulo} com {self.quant}'

    def analisar(self):
        recomendo = self.quant * 0.4
        total = 82.40 * recomendo
        pessoa = total / self.quant
        conteudo = f'Analisando [green]{self.titulo}[/] com [cyan]{self.quant} convidado[/]\n'
        conteudo += 'Cada participante comera 0.4Kg e cada Kg custa R$82.40\n'
        conteudo += f'Recomendo [cyan]comprar {recomendo:.3f}Kg[/] de carne\n'
        conteudo += f'O custo total sera de [green]R${total:.2f}[/]\n'
        conteudo += f'Cada pessoa pagara [yellow]R${pessoa}[/] para participar.\n'
        analisar = Panel(conteudo, title=self.titulo)
        print(analisar)



c1 = Churrasco('Churras dos Amigos', 15)
c2 = Churrasco('Churras do fut', 80)
c1.analisar()
c2.analisar()