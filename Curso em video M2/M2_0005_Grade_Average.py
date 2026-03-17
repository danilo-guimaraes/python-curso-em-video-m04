nota_bimestre_1 = float(input('Qual nota do seu primeiro bimestre?\n'))
nota_bimestre_2 = float(input('Qual nota do seu segundo bimestre?\n'))
media = (nota_bimestre_1 + nota_bimestre_2) / 2
if media < 5.0:
    print(f'REPROVADO COM A MEDIA {media:.1f}')
elif media >= 7.0:
    print(f'APROVADO COM A MEDIA {media:.1f}')
else:
    print(f'Media de {media:.1f}, RECUPERACAO')