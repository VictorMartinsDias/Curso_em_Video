altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura*largura
quantidade = area/2
print('Para pintar uma parede com area de {:.2f}m² vai gastar {:.2f} litros de tinta'.format(area, quantidade))