# 0024 - Script para extrair o primeiro e o último nome de uma pessoa

# Lê o nome e o .strip() remove espaços inúteis no início e no fim
nome = input('Digite seu nome completo: ').strip()

# .capitalize() padroniza a 1ª letra e o .split() transforma o nome em uma LISTA de palavras
nome = nome.capitalize().split()

# O índice [0] acessa sempre o primeiro item da lista (primeiro nome)
primeiro = nome[0]

# O índice [-1] é um atalho do Python para pegar sempre o ÚLTIMO item da lista
ultimo = nome[-1]

# Exibe o resultado usando f-string para inserir as variáveis dentro do texto
print(f'Seu primeiro nome é ({primeiro}) e o seu último sobrenome é ({ultimo})')
