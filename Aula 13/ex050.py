soma = 0
cont = 1

for c in range(0,6):
    n = int(input('Digite o {} número: '.format(cont)))
    if n % 2 == 0:
        soma += n
    cont += 1
print(soma)
