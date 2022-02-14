km = float(input('Quantidade de Km percorridos: '))
d = int(input('Quantidade de dias que o carro foi alugado:'))
p = ( 60* d ) + ( 0.15 * km )

print('Quilômetros: {}\nDias alugado:{}\nPreço a pagar:{:.2f}'.format(km,d,p))
