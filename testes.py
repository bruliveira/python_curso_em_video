nome = str(input('Qual seu nome? '))
if nome == 'Bruna':
    print('Nome massa')
elif nome == 'Flávia' or nome == 'Alves':
    print('Médio em')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Normal')

print('\033[7;31;43m Olá mundo\033[m')
