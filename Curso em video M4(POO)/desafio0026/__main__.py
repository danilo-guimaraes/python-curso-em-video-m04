from M4_DS_026_salario import *
from rich import print, inspect
from rich.table import Table


def main():
    f1 = Horista('Danilo', 25,250)
    f1.calc_salario()
    f1.analisar_sal()

    f2 = Mensalista('Maria', 8500)
    f2.calc_salario()


if __name__ == "__main__":
    main()
