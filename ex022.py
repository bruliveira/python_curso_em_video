#Analizador de texto
nome = str(input('Digite seu nome completo: ')).strip()

sep = nome.split()#divide tudo em ista

print('Nome: ',nome)
print('Nome em maiúsculo: ',nome.upper())
print('Nome em minusculo: ',nome.lower())
print('Total de letras: ',len(nome) - nome.count(' '))
print('Letras no primeiro nome é {} e tem {} letras '.format(sep[0], nome.find(' ')))
print('Letras no primeiro nome é {} e tem {} letras '.format(sep[0], len(sep[0])))