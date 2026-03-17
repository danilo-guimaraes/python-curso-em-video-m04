valor = int(input('Quanto voce quer sacar R$:\t'))
cedula = 50
total_ced = 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cedulas de R$ {cedula}')


        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_ced = 0

        if valor == 0:
            break