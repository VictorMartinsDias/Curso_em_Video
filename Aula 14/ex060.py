n = int(input('Digite um número: '))
fatorial = 1
cont = int(n)
print('Calculando {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial = fatorial * cont
    cont -= 1
print('A soma fatorial de {} é {}'.format(n, fatorial))