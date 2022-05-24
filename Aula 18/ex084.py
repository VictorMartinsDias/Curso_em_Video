temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] '))
        if opcao in 'SsNn':
            break
    if opcao in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo, voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {maior}kg.')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor}kg')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')

