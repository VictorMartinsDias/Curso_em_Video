bo = 's'
n = soma = media = maior = menor = cont = 0
while bo in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    media = soma/cont
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    bo = str(input('Deseja continuar ? [S/N] ')).strip()[0]
print('A média entre os valores foi {}'.format(media))
print('O maior valor foi {} e o menor {}'.format(maior,menor))
