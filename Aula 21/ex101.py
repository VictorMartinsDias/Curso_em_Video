def voto(ano_de_nascimento):
    from datetime import date
    idade = date.today().year - ano_de_nascimento
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade < 65:
        return print('Voto obrigatório ')
    elif 16 <= idade < 18 or idade >= 65:
        return print('Voto opcional')
    else:
        return print('Voto negado')


n = int(input('Em que ano você nasceu? '))
voto(n)
