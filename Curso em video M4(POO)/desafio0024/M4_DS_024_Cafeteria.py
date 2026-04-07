from abc import ABC, abstractmethod
from time import sleep


class BebidaQuente:

    def preparar(self):
        print('--- Iniciando o Preparo ---')
        sleep(1)
        self.fever_agua()
        self.misturar()
        self.servir()
        print('\n--- Bebida Pronta ---\n')

    def fever_agua(self):
        print(f'1.Fervendo agua a 100 graus Celsius')

    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando agua pressurizada pelo po de cafe moido')
        sleep(1)

    def servir(self):
        print('3. Servindo em xicara pequena')
        sleep(1)


class Cha(BebidaQuente):
    def misturar(self):
        print('2. Mergulhando o sache de ervas na agua.')
        sleep(1)

    def servir(self):
        print('3. Servindo na caneca de porcelana')
        sleep(1)


class Leite(BebidaQuente):
    def misturar(self):
        print('2. Passando agua pressurizada pelo bico do leite')
        sleep(1)

    def servir(self):
        print('3. Servindo ena caneca grande ja com cage')
        sleep(1)
