num = int(input('Digite um ano: '))
n = num%4
if n == 0:
    print('O ano {} é bissexto'.format(num))
else:
    print('O ano {} não é bissexto'.format(num))