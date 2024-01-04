peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('CUIDADO! Você está em OBESIDADE')
else:
    print('CUIDADO! Você está em OBESIDADE MÓRBIDA')
