from rich import print


class Canate:
    def __init__(self, cor='azul'):
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case 'preto' | 'preta':
                escolha = '[black]'
            case _:
                escolha = ['white']
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f':prohibited: A {self.cor}caneta[/] esta tampada')
        else:
            print(f'{self.cor}{msg}[/] ', end='')

    def quebrar_linha(self, qtd=1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Canate('vermelha')
c2 = Canate('preto')
c3 = Canate('vermelho')
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever('-' * 30)
c1.quebrar_linha()
c2.escrever('FLAMENGO')
c2.quebrar_linha()
c3.escrever('-' * 30)
c3.quebrar_linha()
c1.escrever('Campeao')

