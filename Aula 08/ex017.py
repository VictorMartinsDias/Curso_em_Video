import math
n = float(input('Comprimento do cateto oposto: '))
n1 = float(input('Comprimento do cateto adjacente: '))
i = math.sqrt((n**2 + n1**2))
print('A hipotenusa vai ser {:.2f}'.format(i))