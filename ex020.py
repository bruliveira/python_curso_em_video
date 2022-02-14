#sorteio com ordem na ista
import random
p = str(input("Digite o primeiro nome: "))
s = str(input("Digite o segundo nome: "))
t = str(input("Digite o terceiro nome: "))
q = str(input("Digite o quarto nome: "))
lista = [ p , s , t , q ]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)
