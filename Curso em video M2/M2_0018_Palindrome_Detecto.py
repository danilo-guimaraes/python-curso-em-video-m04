frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'Temos um palíndromo a frase {junto} ao contrario é {inverso}!')
else:
    print(f'A frase {junto} não é um palíndromo pois fica {inverso}!')

# ------------------------
# Outra opção
# ------------------------

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um palíndromo na frase {junto}')
else:
    print(f'A frase {junto} não é um palíndromo!')

