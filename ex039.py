from datetime import date
atual = date.today().year
an = int(input('Ano de nascimento:'))
idade = atual - an

print('Quem nasceu em {} tem {} anos em {}' .format(an, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, tem apenas {}'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'. format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    print('ERROR')
