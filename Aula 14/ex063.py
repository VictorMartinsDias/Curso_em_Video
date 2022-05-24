n = int(input('Quantos elementos ? '))
cont = 2
n1 = 0
n2 = 1
soma = 0
while cont <= n:
    if cont == 2:
        print('0 -> ', end='')
    print('{} -> '.format(n2), end='')
    soma = n1 + n2
    n1 = n2
    n2 = soma
    cont += 1
print('FIM')

