peso_do_paciente = float(input('Qual seu peso?'))
altura_do_paciente = float(input('Qual sua altura?'))
IMC = peso_do_paciente / altura_do_paciente ** 2
if IMC < 18.5:
    print(f'Abaixo do peso com {IMC:.2f}')
elif IMC > 18.5 and IMC <= 25:
    print(f'PESO IDEAL de{IMC:.2f}')
elif IMC >25 and IMC <= 30:
    print(f'Sobrepeso com IMC de {IMC:.2f} ')
elif IMC >30 and IMC <= 40:
    print(f'OBESIDADE COM IMC de {IMC:.2f}!!!!!')
else:
    IMC > 40
    print(f'OBESIDADE MORBIDA COM IMC de {IMC:.2f}!')