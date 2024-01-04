import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto ajacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
