from M4_DS_025_frete import *
from rich import print, inspect
from rich.table import Table


def main():
    dist = 80

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    """entrega = Drone(dist)
    print(f"Frete de {type(t1).__name__} em {dist}Km custara {t1.calcular_frete()}")"""

    tabela = Table(title='Tabela de frete')
    tabela.add_column('Distancia')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for item in viagem:
        tabela.add_row(f'{dist}Km',f'{type(item).__name__}',f'{item.calcular_frete()}')

    print(tabela)
    t1 = Moto(dist)
    print(f"Frete de {type(t1).__name__} em {dist}Km custara {t1.calcular_frete()}")

    dist = 80
    t2 = Caminhao(dist)
    print(f"Frete de {type(t2).__name__} em {dist}Km - {t2.calcular_frete()}")

    dist = 10
    t3 = Drone(dist)
    print(f"Frete de {type(t3).__name__} em {dist}Km - {t3.calcular_frete()}")


if __name__ == "__main__":
    main()
