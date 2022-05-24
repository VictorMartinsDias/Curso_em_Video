jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
for c in range(0, jogador['partidas']):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} ele fez {v} gols')

