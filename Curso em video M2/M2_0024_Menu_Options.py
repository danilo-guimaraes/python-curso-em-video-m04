numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
menu = 0
maior = 0
while menu != 5:
    menu = int(input(f'''\nO que você quer fazer com o numero {numero_1} e o numero {numero_2}?
    [1] Somar
    [2] Muiltiplicar
    [3] Maior numero entre eles
    [4] Novos numeros
    [5] Sair do programa
: '''))
    if menu == 1:
        print(f'Seu resultado de {numero_1} + {numero_2} é = {numero_1 + numero_2}')
    elif menu == 2:
        print(f'Seu resultado de {numero_1} x {numero_2} é= {numero_1 * numero_2}')
    elif menu == 3:
        if numero_1 > numero_2:
            maior = numero_1
        else:
            maior = numero_2
        if numero_1 == numero_2:
            print('Os dois valores são iguais!')
        else:
            print(f'Entre {numero_1} e {numero_2} o maior valor é {maior}')
    elif menu == 4:
        numero_1 = int(input('Digite o primeiro numero :'))
        numero_2 = int(input('Digite o segundo numero:'))
    elif menu == 5:
        print('Finalizando.....')
    else:
        print('Opção invalida \n')
print('FIM')