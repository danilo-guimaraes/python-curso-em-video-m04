total = mil_reais = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Qual preco do produto: '))
    total += preco
    cont += 1

    if preco >= 1000:
        mil_reais += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print(f'o total da compra foi {total}')
print(f'o produto mais barato foi {barato}')
print(f'{mil_reais} custam mais que R$:1000')
