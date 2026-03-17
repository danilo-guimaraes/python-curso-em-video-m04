numero = int(input('Diga uma numero: '))
total = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{n}, ', end='')
print(f'\n\033[mO numero {numero} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele e PRIMO')
else:
    print('Por isso ele nao e PRIMO')