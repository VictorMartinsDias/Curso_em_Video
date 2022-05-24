pessoa = {}
dados = []
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: F/M ')).strip()[0]
        if pessoa['sexo'] in 'FfMm':
            break
        else:
            print('Digite novamente')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja Continuar? S/N')).strip()[0]
        if opcao in 'SsNn':
            break
        else:
            print('Digite novamente')
    if opcao in 'Nn':
        break
print(dados)
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
média = soma / len(dados)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média:')
for p in dados:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()

