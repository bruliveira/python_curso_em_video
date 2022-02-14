import random
print('------------ JOGO DA ADIVINHAÇÃO -----------')
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10\nSerá que você consegue adivinhar?')
palpite = int(input('Qual seu palpite: '))
numero_escolido = random.randint(0, 10)
tentativas = 0
while palpite != numero_escolido:
    if palpite < numero_escolido:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite: '))
        tentativas += 1
    if palpite > numero_escolido:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite: '))
        tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
