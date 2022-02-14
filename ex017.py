#triangulo retagulo
import math
co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto adjacente: '))
hh = pow(co,2) + pow(ca,2)
h = (co ** 2 + ca **2) **(1/2)
hip = math.hypot(co,ca)
print('\n--------RESULTADOS---------\nCateto oposto: {}\nCateto adjacenDigite um número real: te: {} \nHipotenusa: {}'.format(co,ca,math.sqrt(hh)))
print(h,hip)