print('Gerador de PA')
print('-'*10)
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1

while c < 11:
    print('{} -> '.format(n), end='')
    n = n + r
    c += 1
print('FIM')

