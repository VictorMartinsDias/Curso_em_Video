peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
IMC = peso/(altura**2)
if IMC<18.5:
    print('Abaixo do Peso')
elif IMC>=18.5 and IMC<25:
    print('Peso Ideal')
elif IMC>=25 and IMC<30:
    print('Sobrepeso')
elif IMC>=30 and IMC<40:
    print('Obesidade')
elif IMC>=40:
    print('Obesidade mórbida')


