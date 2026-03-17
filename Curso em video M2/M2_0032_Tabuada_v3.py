from time import sleep

t = 0
while True:
    print('-' * 30)
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    sleep(0.5)

    soma = f'''
{t} x 1 = {t * 1}
{t} x 2 = {t * 2}
{t} x 3 = {t * 3}
{t} x 4 = {t * 4}
{t} x 5 = {t * 5}
{t} x 6 = {t * 6}
{t} x 7 = {t * 7}
{t} x 8 = {t * 8}
{t} x 9 = {t * 9}
{t} x 10 = {t * 10}'''
    if t < 0:
        break
    print(f'{soma}')

print(f'Voce digitou os valores {t}, fim\t do\t programa'.upper())
