from time import sleep

def linha(com, fim, pulo):
    print('-'*30)
    print(f'Contagem de {com} até {fim} de {pulo} em {pulo}')


def contador(inicio, fim, passo):
    linha(inicio, fim, passo)
    valor = inicio
    while valor <= fim:
        print(f'{valor}', end=' ')
        valor += passo
        sleep(1)
    print('FIM!')


linha(1, 10, 1)
for c in range(1, 11):
    print(c, end=' ')
    sleep(1)
print('FIM')
linha(10, 0, 2)
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(1)
print('FIM')

print('-'*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
