maior = homens = mulheres = 0
c = 1
opcao = 'S'
while True:
    if opcao == 'S':
        idade = int(input(f'Digite a idade da {c} pessoa: '))
        sexo = str(input(f'Digite o sexo da {c} pessoa: [M/F] ' )).strip().upper()[0]
        c += 1
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F':
            if idade <= 20:
                mulheres += 1
        while True:
            opcao = str(input('Você deseja continuar? S/N ')).strip().upper()[0]
            if opcao in 'SN':
                break
    else:
        break
print(f'O número de pessoas com mais de 18 anos é {maior}')
print(f'O número de homens ccadastrados é {homens}')
print(f'O número de mulheres com menos de 20 anos é {mulheres}')
