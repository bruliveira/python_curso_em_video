n = int(input('Digite um número: '))
numerosdi = 0
soma = 0
while n != 999:
    numerosdi += 1
    soma = soma + n
    n = int(input('Digite um número: '))
print('---------- RESULTADOS --------')
print(f'O total de números digitados foi: {numerosdi}')
print(f'A soma de todos os números é: {soma}')
