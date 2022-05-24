n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n !=999:
        cont += 1
        soma += n
print('A soma de {} termos foi {}'.format(cont, soma))
