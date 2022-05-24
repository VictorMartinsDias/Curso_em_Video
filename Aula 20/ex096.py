def area(l, c):
    a = l*c
    print(f'A area de um terreno {l:.1f}x{c:.1f} é de {a:.2f}m²')


print('Controle de Terrenos')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

