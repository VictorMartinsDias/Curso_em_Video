import math
n = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O ângulo {:.2f}° tem o seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(n, s, c, t))