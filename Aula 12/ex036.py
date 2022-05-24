valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos para pagar? '))
pres = valor/(anos*12)
salario3 = salario*3/10
if pres > salario3:
    print('Emprestimo negado')
else:
    print('O empréstimo vai ser disponibilizado em {} anos, com prestações de R${:.2f}'.format(anos, pres))


