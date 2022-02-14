vc = float(input('\033[1;36mQual o valor da casa? '))
s = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos vai pagar?\033[m'))

ms = anos * 12
prestacao = vc / ms
ps = (s * 0.30)

print('\n\033[1;35mPara pagar a casa de R${:.2f} em {} anos,'.format(vc, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if ps >= prestacao:
    print('\033[1;32mEmpréstimo aprovado')
else:
    print('\033[1;31mEmpréstimo Negado')

