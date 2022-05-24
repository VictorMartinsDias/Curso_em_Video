from datetime import date
ano = date.today().year
nasc = (int(input('Digite o ano do seu nascimento: ')))
idade = ano-nasc
if(idade<=9):
    print('MIRIM')
elif(idade>9 and idade<=14):
    print('INFANTIL')
elif(idade>14 and idade<=19):
    print('JÚNIOR')
elif(idade>=20):
    print('MASTER')