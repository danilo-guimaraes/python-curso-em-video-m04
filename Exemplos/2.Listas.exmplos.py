num = [2,5,9,1]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
# num.pop(2)
num.remove(1)
if 4 in num:
    num.remove(4)
else:
    print(f'O numero nao esta na lista')
print(num)
print(num)
print('Essa lista tem {} elementos'.format(len(num)))

valores = list()
for c in range(0,5):
    valores.append(int(input('digite um valor: ')))
for c, v in enumerate (valores):
    print(f'na posicao {c} encontrei o valor {v}')
print('fim da lista')

a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista A + B: {a+b}')


# -------PART2------
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['Joao',19],['Ana',33],['Joaquim', 13],['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')

galera = []
dados = []
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite uma idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')