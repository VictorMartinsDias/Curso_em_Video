import random

itens = ('Pedra', 'Papel', 'Tesoura')

computador = random.randint(0,2)
print('0 - Pedra\n1 - Papel\n2 - Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('Jokenpô')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 0:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 0:
        print('Computador venceu')
    else:
        print('Jogada inválida')