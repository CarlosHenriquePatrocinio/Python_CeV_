listagem = ('pão', 1,
            'leite', 3.50,
            'frango', 10.90)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
        