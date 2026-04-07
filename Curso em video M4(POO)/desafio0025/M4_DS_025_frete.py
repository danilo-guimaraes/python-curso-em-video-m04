from rich import print
from abc import ABC, abstractmethod


class Tranpsorte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Tranpsorte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R${self.frete:.2f}'


class Caminhao(Tranpsorte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Raio minimo de 50KM"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R${self.frete:.2f}'

class Drone(Tranpsorte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return 'Raio maximo de 10Km'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R${self.frete:.2f}'
