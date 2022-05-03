from math import sqrt

x1=float(input('Digite o número x1: '))
x2=float(input('Digite o número x2: '))
x3=float(input('Digite o número x3: '))
y1=float(input('Digite o número y1: '))
y2=float(input('Digite o número y2: '))
y3=float(input('Digite o número y3: '))
    
dis1=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
dis2=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
dis3=sqrt(pow(x3-x2,2)+pow(y3-y2,2))

cond1= True
cond2=True
cond3= True

if dis1==0 or dis2==0 or dis3==0: 
    cond1=False

if dis1>(dis2+dis3) or dis2>(dis1+dis3) or dis3>(dis1+dis2):
    cond2=False

if dis1<=abs(dis2-dis3) or dis2<=abs(dis1-dis3) or dis3<=abs(dis1-dis2):
    cond3=False

tringulo=True

if cond1==False or cond2==False or cond3==False:
    print('Nenhum triângulo formado com os pontos informados')

    if cond1==False:
        print('Pelos menos um dos lados é igual a zero.')
    if cond2==False:
        print('Pelo menos um dos lados é maior que a soma dos outros dois lados.')
    if cond3==False:
        print('Pelo menos um dos lados é menor ou igual ao módulo da diferença.')


elif dis1==dis2==dis3:
        print('Será um triangulo equilátero.')
elif dis1!=dis2==dis3:
        print('Será um triangulo isóceles')
elif dis1!=dis2!=dis3:
        print('Será um triangulo escaleno.')

if tringulo:
    print('Medida do lado 1: {:.2f}, medida do lado 2: {:.2f}, medida do lado 3: {:.2f}.'.format(dis1,dis2,dis3))

