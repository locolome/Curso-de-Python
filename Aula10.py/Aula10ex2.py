x1=float(input('Digite a reta 1:'))
x2=float(input('Digite a reta 2:'))
x3=float(input('Digite a reta 3:'))
if x1<x2+x3 and x2<x1+x3 and x3<x2+x1:
    print('Pode formar um triângulo')
    if x1==x2==x3:
        print('Será formado um triângulo equilátero.')
    if x1==x2!=x3 or x3==x1!=x2 or x3==x2!=x1:
        print('Será um triângulo isóceles')
    if x1!=x2!=x3!=x1:
        print('Será um triângulo escaleno.')
else:
    print('Não pode formar um triângulo')

