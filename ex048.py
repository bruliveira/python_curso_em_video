s = 0
for n in range(1, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            s = s + n
            print(n)
print('Soma: ', s)
