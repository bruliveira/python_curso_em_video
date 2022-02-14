cbf = ('Internacional', 'São Paulo', 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Ceará', 'Corinthians', 'Santos', 'Bragantino', 'Athletico-PR', 'Atlético-GO', 'Vasco', 'Sport', 'Fortaleza', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
print('----------------- RESULTADOS -------------')
print('5 primeiros colocados: ', cbf[0:5])
print('4 últimos colocados: ', cbf[-4:])
print('Times em ordem: ', sorted(cbf))
print(f'Bahia posição: {cbf.index("São Paulo")+1} posição')

time = str(input('Digite qual time você quer saber a posição:'))
for cont in range(0, len(cbf)):
    if cbf[cont] == time:
        print(f'{time} está na {cont + 1}° posição')