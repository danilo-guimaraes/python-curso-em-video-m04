from rich import print
from rich.panel import Panel

caixa = Panel('[black on red]FLAMENGO[/]'.center(93),title='MELHOR TIME', style='red on black')

print(caixa)