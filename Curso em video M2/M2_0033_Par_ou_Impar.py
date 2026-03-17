from random import randint

vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    print('=-'*10)
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou!')
            vitorias += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce ganhou!')
            vitorias += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Voce jogou {vitorias} vezes')