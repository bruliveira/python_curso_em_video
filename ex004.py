#Dissecando uma variavel
n = input('Digite algo: ')

print(type(n))

print('É um numero:', n.isnumeric())
print('É alfabetico:', n.isalpha())
print('É alfanumerico:', n.isalnum())
print('Caracteres com espaço:', n.isspace())
print('Todos caracteres minusculos:', n.islower())
print('Todos caracteres maiusculos:', n.isupper())
print('Aceita perimetros:', n.isprintable())
