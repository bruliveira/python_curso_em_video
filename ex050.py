s = 0
for c in range(0, 6):
    n = int(input('Digite um número par: '))
    if n % 2 == 0:
        s += n
    else:
        n = int(input('Digite um número que seja par: '))
        s += n
print(s)