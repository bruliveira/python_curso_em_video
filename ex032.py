from datetime import date
from termcolor import colored
ano = int(input("Qual ano você quer analisar(Coloque 0 para o atual)? "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(colored("{} é um ano bissexto".format(ano), 'green'))
else:
    print(colored("{} não é um ano bissexto".format(ano), 'red'))

