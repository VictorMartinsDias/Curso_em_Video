num = int(input('Digite um número inteiro: '))
n = num%2
if n == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))