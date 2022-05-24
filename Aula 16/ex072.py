num_ext = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    c = int(input('Digite um número de 1 a 20: '))
    if 1 <= c <= 20:
        break
    print('Tente novamente.', end=' ')
print(num_ext[c-1])
