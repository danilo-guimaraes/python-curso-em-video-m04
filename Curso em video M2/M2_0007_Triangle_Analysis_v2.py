reta_do_triangulo_1 = int(input('Digite o valor da primeira reta: '))
reta_do_triangulo_2 = int(input('Digite o valor da segunda reta: '))
reta_do_triangulo_3 = int(input('Digite o valor da terceira reta: '))

if (reta_do_triangulo_1 < reta_do_triangulo_2 + reta_do_triangulo_3
        and reta_do_triangulo_2 < reta_do_triangulo_1 + reta_do_triangulo_3
        and reta_do_triangulo_3 < reta_do_triangulo_1 + reta_do_triangulo_2):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

    if reta_do_triangulo_1 == reta_do_triangulo_2 == reta_do_triangulo_3:
        print('EQUILÁTERO!')
    elif reta_do_triangulo_1 != reta_do_triangulo_2 != reta_do_triangulo_3 != reta_do_triangulo_1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')


else:
 print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
