import random
import time
n = random.randint(0 ,5)
nd = int(input('Digite um número inteiro entre 0 a 5: '))
time.sleep(5)
if nd == n:
    print('Parabéns você acertou, o número é {}'.format(n))
else:
    print('Você errou, o número é {}'.format(n))