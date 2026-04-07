from M4_DS_023_Poligonos import Quadrado, Circulo
from rich import print, inspect


def main():
    """Cria instâncias de Quadrado e Circulo e exibe perímetro e área de cada um."""
    q = Quadrado(21)
    # inspect(q, methods=True)
    print(f'Um quadrado de lado {q.lado}cm tem perimetro de {q.perimetro():.1f}mm')
    print(f'Um quadrado de lado {q.lado}cm tem area de {q.area()}mm²')

    c = Circulo(40)
    print(f'Um circulo de raio {c.raio}cm tem area de {c.perimetro():.1f}cm²')
    print(f'Um circulo de raio {c.raio}cm tem area de {c.area():.1f}cm²')


if __name__ == '__main__':
    main()

