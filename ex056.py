totalidade = 0
maisvelho = ''
maioridadehomem = 0
totmulher = 0
for nis in range(1, 5):
    print('------- ', nis, '° pessoa -------')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[F/M]:'))
    totalidade = totalidade + idade
    if nis == 1 and sexo in 'Mm':
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

print('---------- RESULTADOS ------------')
print('A média de idade é: ', totalidade/4)
print('O homem mais velho é: ', maisvelho)
print(totmulher, ' mulheres acimas de 20 anos')
