while True:
    print('Banco do Victor')
    sacar = int(input('Quanto que você deseja sacar? R$'))
    nota50 = sacar//50
    resto50 = sacar%50
    nota20 = resto50//20
    resto20 = resto50%20
    nota10 = resto20//10
    resto10 = resto20%10
    nota1 = resto10
    break
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota1 != 0:
    print(f'Total de {nota1} cédulas de R$1')
print('Volte sempre!')