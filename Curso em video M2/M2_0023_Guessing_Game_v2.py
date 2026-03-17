from random import randint

cpu_number = int(randint(0, 10))
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('Escolha um palpite: '))
    palpites += 1
    if jogador == cpu_number:
        acertou = True

print('Parabéns você acertou!!!!')
print(f'Foram {palpites} palpites')