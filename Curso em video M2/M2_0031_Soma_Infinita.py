n = s = v = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    v = v + 1

    if n == 999:
        break
    s += n
print(f'A soma dos {v - 1} vale {s}')