import math
from abc import ABC, abstractmethod


class Poligono(ABC):
    """Classe abstrata base para polígonos. Não pode ser instanciada diretamente."""

    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        """Retorna o perímetro do polígono. Deve ser implementado pelas subclasses."""
        pass

    @abstractmethod
    def area(self) -> float:
        """Retorna a área do polígono. Deve ser implementado pelas subclasses."""
        pass


class Quadrado(Poligono):
    """Polígono de 4 lados iguais."""

    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        """Retorna o perímetro: lado × 4."""
        return self.lado * 4

    def area(self):
        """Retorna a área: lado²."""
        return self.lado ** 2


class Circulo(Poligono):
    """Figura circular. Usa 0 lados por convenção."""

    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        """Retorna a circunferência: 2 × π × raio."""
        return 2 * math.pi * self.raio

    def area(self):
        """Retorna a área: π × raio²."""
        return math.pi * self.raio ** 2