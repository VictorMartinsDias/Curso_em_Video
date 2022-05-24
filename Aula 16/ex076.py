lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.9)
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)
c = 0
while c <= len(lista):
    print(f'{lista[c]:.<40}', end='')
    print(f'R$ {lista[c+1]:>7.2f}')
    c += 2
