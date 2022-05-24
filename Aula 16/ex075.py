num = (int(input('digite um número: ')),
       int(input('digite um número: ')),
       int(input('digite um número: ')),
       int(input('digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 aparareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
       print(f'O valor 3 não apareceu em nenhuma posição')
print(f'O valores pares digitados foram ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')


