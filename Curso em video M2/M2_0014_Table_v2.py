from time import sleep

numero = int(input('Digite um numero: '))
for tabuada in range (1, 10 + 1 ):
    resultado = tabuada * numero
    sleep(0.4)
    print(f'{numero} x {tabuada} = {resultado}')
print('Acabou')