primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
if primeiro_numero > segundo_numero:
    print(f'O seu numero {primeiro_numero} é maior que o numero {segundo_numero}')
elif primeiro_numero < segundo_numero:
    print(f'O seu numero {primeiro_numero} é menor que o numero {segundo_numero}')
else:
    print(f'O numero {primeiro_numero} é igual ao numero {segundo_numero}')