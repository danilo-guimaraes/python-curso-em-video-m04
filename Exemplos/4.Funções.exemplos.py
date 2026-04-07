# def mensagem(msg):
#     print('-=' * 30)
#     print(msg)
#     print('-=' * 30)
#
#
# mensagem(msg='Boa noite')
# mensagem(msg='Como vai?')
#
#
# def soma(a, b):
#     print("A soma de {} e {}".format(a, b))
#     s = a + b
#     print(f'A soma de {a} e {b} = {s}')
#     print()
#
#
# # soma(4,5)
# # soma(8, 9)
# # soma(2, 1)
# n1 = int(input('digite um numero: '))
# n2 = int(input('digite outro numero: '))
# soma(n1, n2)
#
# def contador(*numeros):
#     for valor in numeros:
#         print(f'{valor} ', end='')
#         tamanho = len(numeros)
#         print(f'Recebi os numeros {numeros} e {tamanho} Numeros')
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
#
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)
#
# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores}, temos {s}')
#
#
# soma(5, 2)
# soma(2, 9, 4)
# # -----------PARTE 2-----------#
# help(print) #COMANDO HELP
# print(input.__doc__)
#
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i:inicio da contagem
#     :param f:fim da contagem
#     :param p:passo da contagem
#     :return:sem retorno
#     BY: Danilo Guimaraes
#     """
#     c=i
#     while c<=f:
#         print(c, end=" ")
#         c += p
#     print("FIM")
#
#
# help(contador)
#
# # ---- Parametros Opcionais -----#
#
# def soma3(a=0,b=0,c=0):
#     """
#
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     soma = a + b + c
#     print(f'A soma vale {soma}')
# soma3(3,2,4)
# soma3(3,2)
# soma3(3)
# soma3(b=10,c=20)
#
# # ---- ESCOPO DE VARIÁVEIS -----#
#
# def teste():
#     x = 8 # ESCOPO LOCAL
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
#
# n = 10 # ESCOPO GLOBAL
# print(f'No programa principal, n vale {n}')
# teste()
#
# def funcao():
#     n1 = 4
#     print(f'N1 local: {n1}')
#
# n1 = 2
# funcao()
# print(f'N1 global vale {n1}')
#
# # ---- RETORNO DE VALORES -----#
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
# print(f'Os resultados foram {r1}, {r2} e {r3}')
#
#
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# # n = int(input('Digite um numero: '))
# # print(f'O fatoriral de {n} = {fatorial(n)}')
# print(f'Os resultados sao {f1},{f2},{f3}')
#
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num = int(input('Digite um numero:'))
# if par(num):
#     print('É par!')
# else:
#     print('É impar!')