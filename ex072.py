extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

op = 'S'
while op == 'S':
    while True:
        numusu = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numusu <= 20:
            break
        print('Tente novamente.', end='')
    print(f'Você digitou o número {extenso[numusu]}')
    op = str(input('Deseja continuar a digitar: ')).strip().upper()[0]
print('Tchauuuuu!')