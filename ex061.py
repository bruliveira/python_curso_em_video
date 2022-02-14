print('---------- GERADOR DE PA ------------')
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
pa = pt
while c < 10:
    print(f'{pa} ➜ ', end='')
    pa = pa + r
    c += 1
print('Fim')
