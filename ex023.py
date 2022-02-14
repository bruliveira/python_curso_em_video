#Separando digitos de numeros
dig = int(input('Digite um número de quatro dígitos: '))
u = dig // 1 % 10
d = dig // 10 % 10
c = dig // 100 % 10
m = dig // 1000 % 10
print('Analisando número {}'.format(dig))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))



