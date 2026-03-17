from datetime import date
ano_de_nascimento_do_atleta = int(input('Qual ano do seu nascimento?\n'))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento_do_atleta
if idade < 9:
    print(f'MIRIM {idade}')
elif idade > 9 and idade <= 14 :
    print(f'INFANTIL {idade}')
elif idade >14 and idade <= 19:
    print(f'JUNIOR {idade}')
elif idade > 19 and idade <= 25:
    print(f'SENIOR {idade}')
else:
    print(f'MASTER {idade}')