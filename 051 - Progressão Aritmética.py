prim = int(input('Primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
dec = prim + (10 - 1) * raz  # Fórmula do enésimo termo de uma PA.
for c in range(prim, dec, raz):
    print(f'{c}', end=', ')
print('Fim.')
