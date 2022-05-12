from ex0 import *
escolha=int(input('Escolha uma das opções: \n1.soma \n2.subtração \n3.divisão \n4.multiplicação \n5.todas as operações '))
num1=int(input('Digite o 1º número: '))
num2=int(input('Digite o 2º número: '))

if escolha<0 or escolha>5:
    esc=int(input('Opção inválido'))
elif escolha==1:
    s=soma(num1,num2)
    print(f'A soma dos dois números é {s}.')
elif escolha==2:
    su=subtracao(num1,num2)
    print(f'A subtração dos dois números é {su}.')
elif escolha==3:
    d=divisao(num1,num2)
    print(f'A divisão dos dois números é {d}')
elif escolha==4:
    m=multiplicacao(num1,num2)
    print(f'A multiplicação dos dois números é {m}')
elif escolha==5:
    c=calculadora(num1,num2)
    print(f'Soma={c[0]} \nSubtração={c[1]} \nMultiplicação={c[3]} \nDivisão={c[2]}')
