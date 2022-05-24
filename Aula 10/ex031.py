d = float(input('Qual a distância da viagem? '))
if d > 200:
    valor = d*0.45
else:
    valor = d*0.50
print('O valor da passagem vai ser R${:.2f}'.format(valor))