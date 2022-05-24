import datetime
anoatual = datetime.date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = (anoatual-ano)
if(idade<18):
    print('Você ainda vai se alistar ao serviço militar, só daqui a {} anos'.format(18-idade))
elif(idade==18):
    print('É a hora de se alistar')
elif(idade>18):
    print('Você passou do tempo de se alistar ao serviço militar, já passou {} anos'.format(idade-18))
