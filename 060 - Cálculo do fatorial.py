n = int(input('Descubra o fatorial de um número: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    f *= c
    c -= 1
    print(' x ' if c > 1 else ' = ', end='')
print(f'{f}')
