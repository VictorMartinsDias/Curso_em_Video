n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Difite o segundo valor: '))
menu = 0
while menu != 1:
    print('[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos números \n[5] - Sair do programa')
    opcao = int(input('Digite uma opcao: '))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    if opcao == 2:
        mult = n1*n2
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
    if opcao == 3:
        if n1 > n2:
            print('O {} é maior que o {}'.format(n1,n2))
        elif n1 < n2:
            print('O {} é maior que o {}'.format(n2,n1))
        elif n1 == n2:
            print('Os números digitados são iguais')
    if opcao == 4:
        n1 = int(input('Digite um novo valor para o primeiro número: '))
        n2 = int(input('Digite um novo valor para o segundo número: '))
    if opcao == 5:
        menu = 1


