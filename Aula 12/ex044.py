preço = float(input('Qual o preço do produto? R$'))
print('1 - dinheiro/cheque \n2 - Cartão \n3 - 2x no cartão \n4 - 3x ou mais no cartão')
opcao = int(input('Qual vai ser a forma de pagamento? '))
if opcao == 1:
    valor = preço-(preço)*10/100
elif opcao == 2:
    valor = preço-(preço)*5/100
elif opcao == 3:
    valor = preço
elif opcao == 4:
    valor = preço+(preço)*20/100
else:
    print('Digite a forma de pagamento')
    valor = 0
if valor != 0:
    print('O valor vai ser de R${:.2f}'.format(valor))

