import random

numero = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
numero1 = random.choice(numero)
numero2 = random.choice(numero)
numero3 = random.choice(numero)
numero4 = random.choice(numero)

if numero1 > numero2:
    maiorp = numero1
    menorp = numero2
else:
    maiorp = numero2
    menorp = numero1

if numero3 > numero4:
    maiors = numero3
    menors = numero4
else:
    maiors = numero4
    menors = numero3

if maiors > maiorp:
    maior = maiors
else:
    maior = maiorp

if menorp < menors:
    menor = menorp
else:
    menor = menors

print('------------- RESULTADOS ---------------')
print(f'Os valores sorteados foram: {numero1}  {numero2}  {numero3}  {numero4}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')

