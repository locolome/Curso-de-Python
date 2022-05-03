a=int(input('Informe o número a: '))
b=int(input('Informe o número b: '))
soma=0
if a<b:
    for c in range(a,b):
        soma+=c
    print(f'A soma dos números entre {a} e {b} é {soma}')
else:
    print('\033[31mErro!\033[m')