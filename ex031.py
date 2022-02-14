from termcolor import colored

d = float(input(colored("Qual a distância da viagem:  ", "blue")))
curtas = 0.50 * d
longas = 0.45 * d

if d <= 200:
    print("você percorreu {}KM, o valor da passagem será: {}".format(d, curtas))
else:
    print("Você percorreu {}KM, o valor da passagem será: {}".format(d, longas))
