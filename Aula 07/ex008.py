n1 = float(input('Uma distância em metros: '))

print('A medida de {:.1f}m corresponde a:'.format(n1))
print('{:.3f}km'.format((n1/1000)))
print('{:.2f}hm'.format((n1/100)))
print('{:.1f}dam'.format((n1/10)))
print('{:.1f}dm'.format((n1*10)))
print('{:.1f}cm'.format((n1*100)))
print('{:.1f}mm'.format((n1*1000)))
