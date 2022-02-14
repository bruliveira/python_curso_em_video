s = ''
while s != 'F' and s != 'M':
    s = str(input('Digite um sexo válido(M ou F): ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso')
