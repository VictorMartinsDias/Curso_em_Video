n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaço? ', n.isspace())
print('É um número?,', n.isnumeric())
print('É um alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizado? ', n.istitle())

