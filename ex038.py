n1 = int(input('\033[1:36mDigite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: \033[m'))

if n1 > n2:
    print('\n\033[1:34mO primeiro valor {} é MAIOR que o segundo {} '.format(n1, n2))
elif n2 > n1:
    print('\n\033[1:34mO segundo valor {} é MAIOR que o primeiro {} '.format(n2, n1))
elif n1 == n2:
    print('\n\033[1:34mO primeiro valor {} e o segundo {} são IGUAIS'.format(n1,n2))
else:
    print('\n\033[1:34mErro no sistema, sorry ')
