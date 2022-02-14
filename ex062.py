print('---------- GERADOR DE PA ------------')
print('-=-' * 20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0
pa = pt
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print(f'{pa} ➜ ', end='')
        pa = pa + r
        cont += 1
    print('Fim')
    mais = int(input('Quantos termos a mais deseja ver? '))
print('Fim')
