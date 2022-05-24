def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa Principal
nome = str(input('Nome do Jogador: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'
ficha(nome, gols)
