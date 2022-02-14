numero = int(input('\033[1:34mDigite um número inteiro: '))
print('\033[1:34m-' * 50)
print('Escolha uma das bases abaixo:')
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
print('-\033[m' * 50)
op = int(input('\n\033[1:35mQual será a base de conversão desejada: \033[1:33m'))

if op == 1:
    print('\n{} convertido para BINÁRIO é igual a {}'. format(numero, bin(numero)[2:]))
elif op == 2:
    print('\n{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif op == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE')
