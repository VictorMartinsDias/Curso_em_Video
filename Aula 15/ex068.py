from random import randint
c = 0

while True:
    esc = str(input('Você que par ou impar? [P/I] ')).strip().upper()[0]
    nc = randint(0,10)
    np = int(input('Digite um número: '))
    s = (np + nc)
    print(f'Você jogou {np} e o computador {nc}, a soma foi {s}')
    if (s % 2) == 0:
        op = 'P'
    else:
        op = 'I'
    if esc == op:
        print('Você ganhou!')
        c += 1
    else:
        print('Você perdeu!')
        if c >= 1:
            print(f'Você teve {c} vitórias consecutivas')
        break


