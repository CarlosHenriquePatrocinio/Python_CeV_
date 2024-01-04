frase = str(input('Digite uma frase: ')).strip().upper()
palavras = (frase.split())
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'A frase {frase} ao contrário é {inverso}.')
if inverso == junto:
    print(f'Temos um palíndromo.')
else:
    print(f'A frase não é um palíndromo.')
