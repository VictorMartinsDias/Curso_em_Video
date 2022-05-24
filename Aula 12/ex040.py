nome = str(input('Digite seu nome: '))
n1 = float(input('Digite a primaeira nota:'))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2
print('A nota do {} foi {:.2f}, logo ele está '.format(nome, média), end='')
if(média<5):
    print('REPROVADO')
elif(média>5 and média<7):
    print('de RECUPERAÇÂO')
elif(média>7):
    print('APROVADO')