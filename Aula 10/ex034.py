sal = float(input('Qual é o seu salário? R$'))
if sal > 1250:
    salario = sal*(1/10)+sal
else:
    salario = sal*(15/100)+sal
print('O seu novo salário com aumento vai ser R${:.2f}'.format(salario))