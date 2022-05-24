cont = 0
soma = 0
velho = 0
nomevelho = ''

for c in range(1,5):
    print('----- {}° pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma = soma + idade
    if sexo in 'Mm':
        if velho < idade:
            nomevelho = nome
            idadevelho = idade
            velho = idade
    elif sexo in 'Ff':
        if idade <= 20:
            cont += 1

media = soma/4
print('A média de idade do grupo é {:.2f}'.format(media))
print('O homem mais velho é o {} com {} anos'.format(nomevelho, idadevelho))
print('O número de mulheres com menos de 20 anos é {}'. format(cont))