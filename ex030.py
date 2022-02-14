
from termcolor import colored
frase = str(input('Digite uma frase: ')).lower().strip()
print(colored("-=-","green")*20)

print('A letra A aparece {} vezes '.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('a')+1))
print('\033[31m'+'escrever aqui'+'\033[0;0m')


