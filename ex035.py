print('-='*20)
print('Analisador')
print('-='*20)

r1 = float(input('\033[0;36;47mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os  segmentos aanimas PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÂO PODEM ORMAR triângulo')