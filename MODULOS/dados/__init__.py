from MODULOS import interface


def leiadinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO!!! VALOR NAO VALIDO\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(valor):
    while True:
        try:
            n= int(input(valor))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!!! VALOR NAO VALIDO\033[m')
            continue
        except (KeyboardInterrupt, SystemExit):
            print('\033[0;31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


def leiafloat(valor):
    while True:
        try:
            n= float(input(valor))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!!! VALOR NAO VALIDO\033[m')
            continue
        except (KeyboardInterrupt, SystemExit):
            print('\033[0;31mO usuario prefiriu nao digitar esse valor\033[m')
            return 0
        else:
            return n
