n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0

while op != 5:
    print('\n---------- MENU PRINCIPAL -------------')
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa')
    op = int(input('Digite a opção desejada:'))

    if op == 1:
        soma = n1 + n2
        print(f'A soma de {n1} mais {n2} é : {soma}')
    if op == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é: {multiplicacao}')
    if op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        if n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'{n1} e {n2} são iguais')
    if op == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    if op > 5:
        print('Opção inválida')
print('Você saiu do programa. TCHAUUUUU!')
