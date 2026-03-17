soma = 0
cont = 0
for contador in range(0, 6):
    cont = int(input('Digite seu numero: '))
    if cont % 2 == 0:
        soma += cont
        print(f'Seu numero {cont} é par')
print(f'Total de seu numeros pares é de {soma}')