somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and Sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if Sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if Sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f'A media da idade do grupo e {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho.capitalize()}')
print(f'Ao todo sao {totmulher20} com mais de 20 anos')