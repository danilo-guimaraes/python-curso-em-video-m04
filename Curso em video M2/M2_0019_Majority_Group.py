from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for id in range (0,7):
    nascimento = int(input('Qual ano do seu nascimento? ').strip())
    idade = (ano_atual - nascimento)
    if idade > 21 :
        maior += 1
        print(f'Você já maior de idade com {idade} de idade')
    else:
        menor += 1
        print(f'Você é menor de idade com {idade} de idade')
print(f'temos {maior} maiores de idades')
print(f'temos {menor} menores de idades')
