lista = []
impar = []
par = []

while True:
    x = (int(input('Digite um número: ')))
    lista.append(x)
    if (x%2) == 0:
        par.append(x)
    else:
        impar.append(x)
    while True:
        opcao = str(input('Deseja continuar? S/N ')).strip()
        if opcao in 'SsNn':
            break
    if opcao in 'Nn':
        break
print(f'A lista completa: {lista}')
print(f'A lista de pares: {par}')
print(f'A lista de impares: {impar}')