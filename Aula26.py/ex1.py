'''lar=int(input('Digite a largura: '))
com=int(input('digite o comprimento: '))

def area(lar,com):
    return lar*com
print('Área = ' , area(lar,com))'''

def area(larg,comp):
    a=larg*comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')

print('Controle terrenos')
l=float(input('largura (m): ' ))
c=float(input('Comprimentos (m): '))
area(l,c)

