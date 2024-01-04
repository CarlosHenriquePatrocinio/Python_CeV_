from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(''' MENU PRINCIPAL:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} + {num2} é {soma}')
    elif opcao == 2:
        produto = num1 * num2
        print(f'O resultado de {num1} x {num2} é {produto}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os valores novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa! Volte sempre.')
