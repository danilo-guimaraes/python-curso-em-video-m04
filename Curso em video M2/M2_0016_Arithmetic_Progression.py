termo = int(input('Valor do termo: '))
razao = int(input('Valor da razao: '))
decimo = termo + (10 - 1) * razao
for contador in range(termo, decimo + razao, razao):
    print(contador)