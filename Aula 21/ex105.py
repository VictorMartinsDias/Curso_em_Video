def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    media = sum(n)/len(n)
    if media >= 6:
        situação = 'boa'
    else:
        situação = 'ruim'
    dicionario['total'] = len(n)
    dicionario['Maior'] = max(n)
    dicionario['Menor'] = min(n)
    dicionario['Média'] = media
    if sit:
        dicionario['Situação'] = situação
    return dicionario


lista = notas(3.5, 2, 6.5, 2, sit=True)
print(lista)
help(notas)