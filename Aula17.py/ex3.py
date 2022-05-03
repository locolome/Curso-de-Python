
n1=int(input('Digite o valor 1: '))
n2=int(input('Digite o valor 2: '))

opcao=0

while opcao!=5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos númericos
    [5] sair do programa''')
    opcao=int(input('Qual é a sua opção: '))

    if opcao == 1:
        soma=n1+n2
        print('A soma entre {n1} e {n2} = {soma}')
    elif opcao==2:
        produto=n1*n2
        print(f'O produto de {n1} e {n2} é {produto}')
    elif opcao==3:
        if n1>n2:
            maior=n1
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
        else:
            maior=n2
            print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao==4:
        print('Informe Novos números: ')
        n1=int(input('Primeiro número; '))
        n2=int(input('Segundo número: '))
    elif opcao==5:
        print('Finalizando...............................................................')
    else:
        print('Opção inválida.')
    print('#'*10)

print('Fim.......................')
    