from termcolor import colored
s = float(input('Qual o seu salário? '))

if s > 1250:
    ns = (s * 0.10) + s
    print(colored('\nSeu novo valor do salário será: R${}'.format(ns), 'green'))
else:
    ns = (s * 0.15) + s
    print(colored('\nSeu novo valor do salário será: R${}'.format(ns), 'green'))
