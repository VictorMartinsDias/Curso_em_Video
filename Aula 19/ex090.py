aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

