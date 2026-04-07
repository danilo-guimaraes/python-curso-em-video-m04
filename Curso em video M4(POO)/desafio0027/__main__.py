from M4_DS_027_rpg import *
from rich import print, inspect


def main():
    p1 = Guerreiro('BK', randint(100,2000))
    p2 = Mago('SM', randint(100,2000))
    p2.status()
    p1.status()

    p1.atacar(p2, randint(1,3000))
    p2.atacar(p1, randint(1,3000))
    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()
