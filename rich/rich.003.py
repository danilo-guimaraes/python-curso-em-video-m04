from rich import print
from rich.table import Table

tabela = Table(title='Tabela de precos')

tabela.add_column('Nome', justify='left', style='cyan')
tabela.add_column('Preco', justify='center', style='green')

tabela.add_row('Lapis', 'R$1,50')
tabela.add_row('Borracha', 'R$1,50')

print(tabela)