from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior é {max(n)}')
print(f'O menor é {min(n)}')