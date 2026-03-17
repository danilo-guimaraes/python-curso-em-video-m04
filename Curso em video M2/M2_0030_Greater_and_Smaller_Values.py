resp = 'S'
soma = quant = maior = menor = 0

while resp in 'Ss':
    numero = int(input('Digite o numero:'))
    soma += numero
    quant += 1

    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    resp = str(input('Deseja continuar? [S/N] ')).upper()



media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
