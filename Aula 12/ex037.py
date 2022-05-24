num = int(input('Digite um número: '))
print('1 para binário \n2 para octal \n3 para hexadecimal')
con = int(input('Digite a base de conversão: '))
if(con == 1):
    print('Conversão binária do número {}'.format(num))
    bin = str(bin(num))
    print('{} = {}'.format(num, bin[2:]))
elif(con == 2):
    print('Conversão octal do número {}'.format(num))
    oct = str(oct(num))
    print('{} = {}'.format(num, oct[2:]))
elif(con == 3):
    print('Conversão hexadecimal do número {}'.format(num))
    hex = str(hex(num))
    print('{} = {}'.format(num, hex[2:]))

