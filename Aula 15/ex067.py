n = c = 1

while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    while True:
        print(f'{n} x {c} = {(n*c)}')
        c += 1
        if c > 10:
            break
    c = 1
