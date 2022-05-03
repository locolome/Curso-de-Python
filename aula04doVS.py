#Exercicio 1
ba=float(input('Qual a base?'))
al=float(input('Qual a altura?'))
area= (ba*al)/2
print('A área do triangulo é: {} cm²'.format(area))

#Exercicio 2
x1=float(input('Qual o x1?'))
x2=float(input('Qual o x2?'))
y1=float(input('Qual o y1?'))
y2=float(input('Qual o y2?'))
d=((x2-x1)**2+(y2-y1)**2)**0.5
print('A distância é: {}'.format(d))

#Exercicio 3
a= float(input('Qual o valor de a?'))
b= float(input('Qual o valor de b?'))
c= float(input('Qual o valor de c?'))
de=(b**2 )-4*a*c
print('Delta é igual a:{:.2f}'.format(de))

#Exercicio 4
nome=input('Qual o nome do corretor?')
iv=float(input('Qual a quantidade de imóveis vendidos?'))
vt=float(input('Qual o valor total de vendas?'))
sl=1500+ (200*iv) + (vt*0.05)
print('O salário final de {} é: R${:.2f}'.format(nome,sl))

