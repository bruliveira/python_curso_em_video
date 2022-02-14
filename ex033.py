from termcolor import colored
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print(colored('\nO menor valor é: {}'.format(menor), 'red'))
print(colored('O maior valor foi : {}'.format(maior), 'green'))

#if a<b and a < c:
 #   menor = a
#if b<c and b < a:
 #   menor = b
#if c<a and c < b:
 #   menor = c
