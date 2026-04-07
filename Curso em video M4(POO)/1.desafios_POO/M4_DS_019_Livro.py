from time import sleep

from rich import print


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [cyan]Voce acabou de abrir o livro '[purple]{self.titulo}[/]' "
        f"que tem [green]{self.total_paginas} paginas[/] no total. "
        f"Voce agora esta na [yellow]pagina {self.pagina_atual}[/][/cyan]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"[red]pag{self.pagina_atual} :arrow_forward:[/] ", end='')
                sleep(0.3)
                cont += 1
        print(f'[cyan]Voce avancou {cont} paginas e agora esta na [yellow]pagina {self.pagina_atual}[/][/cyan]')
        if self.fim_do_livro():
            print(f":closed_book: [green]Voce chegou ao final do livro '[purple]{self.titulo}[/]'[/green]")

    def fim_do_livro(self)-> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = Livro('O Programador Pragmático', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
