from random import randint

primeiro = int(input('Valor do termo: '))
razao = int(input('Valor da razao: '))
cont = 1
termo = primeiro
random = randint(10,20)
while termo <= random:
    print(f'{termo}->', end='')
    termo += razao
    cont += 1
print(f'{random} Seu termo {primeiro} com a razão {razao} ')