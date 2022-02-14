pp = float(input('Digite um peso: '))
maior = pp
menor = pp
for p in range(0, 4):
    pp = float(input('Digite um peso: '))
    if pp > maior:
        maior = pp
    if pp < menor:
        menor = pp
print('Maior peso é: ', maior)
print('Menor peso é: ', menor)
