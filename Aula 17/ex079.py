lista = []
opcao = 'S'

while opcao in 'Ss':
    n = (int(input('Digite um número: ')))
    while True:
        if opcao in 'Nn':
            break
        x = lista.count(n)
        if x == 0:
            lista.append(n)
            print('Número adicionado com sucesso')
            break
        else:
            n = int(input('Valor duplicado, digite um número: '))
    while True:
        opcao = str(input('Deseja continuar ? S/N ')).strip()
        if opcao in 'SsNn':
            break
lista.sort()
print(f'{lista}')

