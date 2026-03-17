sexo = str(input('Qual seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, novamente Diga seu sexo: ')).upper().strip()
print(f'Sexo {sexo} Registrado com sucesso')