from random import randint

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        print(f'{n}', end=' ')
        lista.append(n)
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)


