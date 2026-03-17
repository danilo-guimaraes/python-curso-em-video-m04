valor = float(input('Qual valor do produto? '))
print('''Formas de pagamentos
[1] a vista dinheiro/cheque
[2] a vista cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao = int(input('Qual e a opcao? '))

if opcao == 1:
    total = valor - (valor * 10/100)
    print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
elif opcao == 2:
    total = valor - (valor * 10/100)
    print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
elif opcao == 3:
    total = valor
    print(f'Sua compra será parcelada em 2x de R${valor:.2f} SEM JUROS.')
elif opcao == 4:
    total = valor + (valor * 2 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.')
    print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')