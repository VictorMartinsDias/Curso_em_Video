print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segemento: '))
if r1 == r2 == r3:
    print('Os segmentos formam um triangulo equilátero')
elif (r1 == r2 or r1 == r2 or r2 == r3) and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triangulo isósceles')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triangulo escaleno')
else:
    print('Os segmentos não podem formar um triângulo')


