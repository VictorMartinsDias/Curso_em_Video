n = int(input('Digite um número pra ver sua tabuada: '))
print('A tabuada do {} é:'.format(n))
for c in range(0,11):
    print('{} x {} = {}'.format(c, n, (n*c)))
