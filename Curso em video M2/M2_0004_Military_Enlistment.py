from datetime import date
ano_do_nascimento = int(input('Qual ano do seu nascimento soldado?'))
data_atual = date.today().year
idade = data_atual - ano_do_nascimento
if idade < 18:
    print(f'Voce tem {idade} ainda ja pode pensar em se alistar soldado!')
elif idade > 18:
    print(f'Voce tem {idade} esta em debito com servico militar pois passou do momento de se alistar!')
else:
    print(f'Com sua idade de {idade} e hora de se alistar soldado, nao fuja!')