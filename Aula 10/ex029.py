vel = float(input('Velocidade do carro: '))
if vel > 80:
    print('Você acaba de ser multado por passar do limite de velocidade de 80 km/h')
    multa = (vel-80)*7
    print('Vai precisar pagar um multa de R${:.2f}'.format(multa))
else:
    print('Continue a ser um motorista que respeita a velocidade')
