num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
 [ 1 ] converter pra BINÁRIO
 [ 2 ] converter pra OCTAL
 [ 3 ] converter pra HEXADECIMAL ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção INVÁLIDA. Tente novamente!')
