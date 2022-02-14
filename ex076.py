listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
n = 'oid'

print('=' * 50)
print('        LISTAGEM DE PREÇOS ')
print('=' * 50)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(listagem[produto], end='.' * 15)
    else:
        print(listagem[produto]);
