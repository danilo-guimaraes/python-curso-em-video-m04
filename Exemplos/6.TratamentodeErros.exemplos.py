# try:
#     a = int(input('Numero inteiro: '))
#     b = int(input('Numero real: '))
#     r = a / b
# except:
#     print('Numero invalido')
# else:
#     print(int(r))
# finally:
#     print('Volte sempre')
#
# try:
#     a = int(input('Numero inteiro: '))
#     b = int(input('Numero real: '))
#     r = a / b
# except Exception as erro:
#     print(f'ERRO: {erro.__class__},{erro.args[0]}')
# else:
#     print(int(r))
# finally:
#     print('Volte sempre')
#
#
# try:
#     a = int(input('Numero inteiro: '))
#     b = int(input('Numero real: '))
#     r = a / b
# except (ValueError, TypeError):
#     print(f'Tivemos um problema com os tipos de dados.')
# except ZeroDivisionError:
#     print('Nao e possivel dividir um numero por zero.')
# except KeyboardInterrupt:
#     print('O usuario prefiriu nao informar os dados.')
# except Exception as erro:
#     print(f'Ocorreu um erro: {erro.__cause__}')
# else:
#     print(int(r))
# finally:
#     print('Volte sempre')
# from time import sleep
#
# from MODULOS.interface import *
#
# while True:
#     resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])
#     if resposta == 1:
#         cabeçalho('Opção 1')
#     elif resposta == 2:
#         cabeçalho('Opção 2')
#     elif resposta == 3:
#         cabeçalho('Sair do Programa, até logo...')
#         break
#     else:
#         cabeçalho('\033[31mERRO! DIGITE UMA OPÇÃO VALIDA!\033[m')
#     sleep(1)