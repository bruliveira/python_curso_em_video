quant = 0
anoatu = int(input('Digite o ano atual: '))
for i in range(0, 7):
    anonas = int(input('Digite o ano de nascimento: '))
    idade = anoatu - anonas
    if idade >= 18:
        quant = quant + 1
print(quant, ', com a maior idade atingida')