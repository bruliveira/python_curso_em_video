#Seno, cosseno e tangente
import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
cosse = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de: {} tem o seno de: {:.2f}'.format(an,seno))
print('O ângulo de: {} tem o cosseno de: {:.2f}'.format(an,cosse))
print('O ângulo de: {} tem o tangente de: {:.2f}'.format(an,tan))
