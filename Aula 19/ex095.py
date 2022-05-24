jogador = {}
partidas = []
lista = []
while True:
    partidas.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
    for c in range(0, jogador['partidas']):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogador['aproveitamento'] = jogador['total'] / jogador['partidas']
    lista.append(jogador.copy())
    while True:
        opcao = str(input('Deseja cadastrar outro jogador? S/N ')).strip().upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

print(f'{"Cod":<5}', end='')
for k in jogador.keys():
    print(f'{str(k):<15}', end='')
print()
for c, v in enumerate(lista):
    print(f'{c:<5}', end='')
    for k in v.values():
        print(f'{str(k):<15}', end='')
    print()
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para sair)'))
    if resp == 999:
        break
    if resp >= len(lista):
        print('Digite novamente')
    elif resp < len(lista):
        print('-- Levantamento do jogador --')
        for i, g in enumerate(lista[resp]['gols']):
            print(f'Na partida {i+1} ele fez {g} gols')

