lista = []
cont = 0
opcao = 'S'
while opcao in 'Ss':
    lista.append(int(input('Digite um número: ')))
    cont += 1
    while True:
        opcao = str(input('Deseja continuar? S/N ')).strip()
        if opcao in 'SsNn':
            break
if 5 in lista:
    x = lista.count(5)
    print(f'O número 5 foi digitado {x} vezes')
else:
    print('O número 5 não foi digitado')
lista.sort(reverse=True)
print(lista)



