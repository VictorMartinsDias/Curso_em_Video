from random import randint
from time import sleep
print('Joga na Mega Sena')
temp = []
jogo = []
w = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, w):
    cont = 1
    while cont < 7:
        n = randint(1 , 60)
        if n not in temp:
            temp.append(n)
            cont += 1
    temp.sort()
    jogo.append(temp[:])
    temp.clear()
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
