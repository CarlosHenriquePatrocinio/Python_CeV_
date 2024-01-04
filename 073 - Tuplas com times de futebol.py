times = ('Atlético', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense',
    'América-MG', 'São Paulo', 'Grêmio', 'Vasco da Gama', 'Botafogo',
    'Sport Recife', 'Cruzeiro', 'EC Vitória', 'Santos', 'Chapecoense',
    'Atlético-PR', 'Internacional', 'Bahia', 'Ceará SC', 'Paraná')
print(f'Lista de times do Brasileirão: \n{times}')
print(f'a) Primeiros 5 colocados: \n{times[0:5]}')
print(f'b) Últimos 4 colocados: \n{times[-4:]}')
print(f'c) Times em ordem alfabética: \n{sorted(times)}')
print(f'd) A Chapecoense está na {times.index('Chapecoense') + 1}ª posição.')
