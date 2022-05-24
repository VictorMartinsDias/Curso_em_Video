import random
import time
n = int(random.randint(0 ,10))
tentativa = int(input('Digite um número inteiro entre 0 a 10: '))
cont = 1
while tentativa != n:
    if tentativa > n:
        print('número é menor')
    elif tentativa < n:
        print('número é maior')
    tentativa = int(input('Você errou, digite novamente um número inteiro entre 0 e 10: '))
    cont += 1
    time.sleep(5)
print('Parabéns você acertou depois de {} tentativas, o número é {}'.format(cont, n))
