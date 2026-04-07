from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod


class Funcionario(ABC):
    salario_minimo = 1_612
    desconto_inss = 7.5

    def __init__(self, nome=None):
        self.nome = nome
        self.bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.salario_minimo

        mensagem = (f'O salario de [blue]{self.nome}[/] [purple]({self.__class__.__name__})[/]\né de [green]R'
                    f'${self.salario:.2f}[/] e corresponde a {base:.1f} '
                    f'salarios minimos.')
        painel = Panel(mensagem,title=f'Salario de {self.nome}', width=50, style='on Black')
        print(painel)



class Horista(Funcionario):
    def __init__(self,nome, valor_hora = 7.37, qtd_hr = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_hr = qtd_hr
        self.bruto = self.qtd_hr * self.valor_hora


    def calc_salario(self):
        self.salario = self.bruto - (self.bruto * Funcionario.desconto_inss / 100)



class Mensalista(Funcionario):
    def __init__(self, nome, bruto = Funcionario.salario_minimo):
        super().__init__(nome)
        self.bruto = bruto
        self.nome = nome

    def calc_salario(self):
        base = self.bruto / Funcionario.salario_minimo
        self.salario = self.bruto - (self.bruto * Funcionario.desconto_inss / 100)
        mensagem = (f'O salario de [blue]{self.nome}[/] [purple]({self.__class__.__name__})[/]\né de [green]R'
                    f'${self.salario:.2f}[/] e corresponde a'
                    f' {base:.1f} '
                    f'salariosinimos.')
        painel = Panel(mensagem, title=f'Salario de {self.nome}', width=50)
        print(painel)