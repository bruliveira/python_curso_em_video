pp = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        pp += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'. format(n, pp))
if pp == 2:
    print('E por isso ele é PRIMO')
else:
    print('e por isso ele não é PRIMO')

