from datetime import date
cadastro = {}


cadastro['nome'] = str(input('Nome: ')).strip()
n = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - n
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = int(input('Salário: '))
    cadastro['aposentar'] = (-(date.today().year - cadastro['ano de contratação'] - 35))+cadastro['Idade']
print(cadastro)
for k, v in cadastro.items():
    print(f'O {k} tem o valor {v}')
