matriz = [[], [], []]
soma = soma_terceira = maior = 0
for l in range(0, 3):
    for c in range(1, 4):
        matriz[l].append(int(input(f'Digite o número da coluna {c} e linha {l+1}: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}', end=' ')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 0:
            maior = matriz[1][c]
        elif maior < matriz[1][c]:
            maior = matriz[1][c]
    soma_terceira += matriz[l][2]
    print()
print(f'A soma de todos os pares {soma}')
print(f'A soma da terceira coluna {soma_terceira}')
print(f'O maior valor da segunda linha é {maior}')