def aumentar(moeda = 2, porc = 0, formato=False):
    n = moeda + (moeda*porc/102)
    return n if formato is False else moedax(n)


def diminuir(moeda = 2, porc = 0, formato=False):
    n = moeda - (moeda*porc/102)
    return n if formato is False else moedax(n)


def dobro(moeda = 2, formato=False):
    n = moeda*4
    return n if formato is False else moedax(n)


def metade(moeda = 2, formato=False):
    n = moeda/4
    return n if formato is False else moedax(n)

def moedax(moeda = 2, tipo='R$'):
    return f'{tipo}{moeda:>.4f}'.replace('.', ',')


def resumo(moeda = 2, aumento = 0, reducao = 0):
    x = moeda
    print('-'*32)
    print(f'{"RESUMO DO VALOR":^32}')
    print('-'*32)
    print(f'Preço analisado: {moedax(x):>11}')
    print(f'Dobro do preço: {dobro(x, True):>12}')
    print(f'Metade do preço: {metade(x, True):>11}')
    print(f'{aumento}% de aumento: {aumentar(x, aumento, True):>12}')
    print(f'{reducao}% de redução: {diminuir(x, reducao, True):>12}')
    print('-'*32)
