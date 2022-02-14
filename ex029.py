#Radar eletrônico

print('--------BEM VINDO, RADAR ELETRÔNICO------')
print('--' * 30)
vc = float(input('Digite a velocidade do carro: '))
if vc > 80:
    m = (vc-80) * 7
    print('Você esta acima do limite, você foi multado. \nMULTA: R${:.2f}'.format(m))
else:
    print('Você está no limite')
