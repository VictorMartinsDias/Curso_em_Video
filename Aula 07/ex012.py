produto = float(input('Qual é o preço do produto? R$ '))
desconto = produto - (produto*5/100)
print('O produto de R${:.2f} fica por R${:.2f} com 5% de desconto'.format(produto, desconto))


