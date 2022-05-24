def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fatorial = 1
    if show == False:
        for c in range(numero, 0, -1):
            fatorial *= c
        return print(fatorial)
    else:
        for c in range(numero, 0, -1):
            if c != 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' ')
            fatorial *= c
        print(f'= {fatorial}')

fatorial(3, False)

help(fatorial)
