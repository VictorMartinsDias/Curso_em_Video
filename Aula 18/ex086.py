matriz = [[], [], []]

for l in range(0, 3):
    for c in range(1, 4):
        matriz[l].append(int(input(f'Digite o número da coluna {c} e linha {l+1}: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}', end=' ')
    print()
