salario = float(input('Qual é o salario do funcionário ? R$'))
reajuste = salario + salario*(15/100)
print('O funcionário que recebia R${:.2f} agora com o aumento de 15% R${:.2f}'.format(salario, reajuste))
