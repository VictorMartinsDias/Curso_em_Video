from datetime import date
ano = date.today().year
cont = 0
cont1 = 0

for c in range(1,8):
    nasc = int(input('Ano de nascimento da pessoa {}: '.format(c)))
    idade = ano - nasc
    if idade>18:
        cont += 1
    else:
        cont1 += 1
print('{} pessoas já são maiores de idade e {} são menores de idade'.format(cont, cont1))