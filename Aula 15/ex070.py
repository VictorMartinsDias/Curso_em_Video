opcao = 'S'
cont = 1
soma = maior = b = 0
barato = ''
while opcao == 'S':
    print(f'----- Produto {cont} -----')
    nome = str(input('Nome:')).strip()
    preco = float(input('Preço: '))
    if cont == 1:
        b = preco
        barato = nome
    cont += 1
    print('-----------------------')
    soma += preco
    if preco >= 1000:
        maior += 1
    if preco < b:
        barato = nome
        b = preco
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print(f'O total de gasto foi R${soma:.2f}')
print(f'O número de produtos que custam mais de R$10000,00 foi {maior}')
print(f'O produto mais barato é o {barato} valendo {b:.2f}')
