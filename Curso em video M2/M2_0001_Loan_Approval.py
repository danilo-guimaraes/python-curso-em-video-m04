vaule_home = float(input('Qual o valor da casa? R$'))
vaule_salary = float(input('Qual o salário do comprador? R$'))
vaule_years = int(input('Em quantos anos ele vai pagar? '))
prestacao = vaule_home / (vaule_years * 12)
if prestacao > (vaule_salary * 0.3):
    print('Empréstimo negado! O valor da prestação é de R${:.2f}, o que excede 30% do salário.'.format(prestacao))
else:
    print('Empréstimo aprovado! O valor da prestação é de R${:.2f}, o que é aceitável para o salário.'.format(prestacao))
