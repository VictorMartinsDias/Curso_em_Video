lista = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    med = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], med])
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip()
        if opcao in 'SsNn':
            break
    if opcao in 'Nn':
        break
print('-'*31)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for c, v in enumerate(lista):
    print(f'{c:<4}', end='')
    print(f'{v[0]:<10}', end='')
    print(f'{v[2]:>8}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')

