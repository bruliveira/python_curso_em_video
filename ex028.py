#jogo da adivinhação
import random
import time
from math import ceil
print('\n--> TENTE ADIVINHAR O NÚMERO QUE O COMPUTADOR ESTÁ PENSANDO ENTRE 0 E 5 <--')
v = int(input('Digite o número que você acha: '))
c = [0, 1, 2, 3, 4, 5] #lista dos numeros
cp = random.choice(c) #o computador escolhe um numero aleatorio
print('PROCESSANDO...')
time.sleep(2)
if v == cp:
    print('Parabéns, você acertou')
else:
    print('Que pena, você errou, o computador pensou em: {}'.format(cp))
