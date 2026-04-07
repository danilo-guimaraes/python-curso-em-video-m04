from random import randint

pessoas = {'Nome': 'Gustavo', 'Sexo': 'Masculino', 'Idade': randint(18, 40)}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Sexo'])
print(pessoas['Idade'])
print(f'Nome:O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} - {v}')

print(pessoas)
pessoas['Nome'] = 'Danilo'
print(pessoas)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo ', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])
print(brasil[0]['sigla'], brasil[1]['sigla'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
    for v in e.values():
        print(f'{v} -', end=' ')
    print()