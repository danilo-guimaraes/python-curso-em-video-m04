from MODULOS.uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat}.')

print(f'O dobro de {num} e {numeros.dobro(num)}')
print(f'O triplo de {num} e {numeros.triplo(num)}')
print(f' E a raiz quadrada de {num} é {numeros.raiz(num):.0f}')
