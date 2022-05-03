#Exercicio 1
b=float(input('Qual a base?'))
a=float(input('Qual a altura?'))
area=b*a/2
print('A área do triangulo é:', area)

#Exercicio 2
x1=float(input('Qual o x1?'))
x2=float(input('Qual o x2?'))
y1=float(input('Qual o y1?'))
y2=float(input('Qual o y2?'))
d=((x2-x1)**2+(y2-y1)**2)**0.5
print('A distância é:', d)

#Exercicio 3
a= float(input('Qual o valor de a?'))
b= float(input('Qual o valor de b?'))
c= float(input('Qual o valor de c?'))
de=(b**2 )-4*a*c
bh1=(-b+ de**(1/2))/(2*a)
bh2=(-b- de**(1/2))/(2*a)
print('O valor da expressão é {}, {}' .format(bh1,bh2))

#Exercicio 4
nome=input('Qual seu nome?')
iv=float(input('Qual a quantidade de imóveis vendidos?'))
vt=float(input('Qual o valor total de vendas?'))
sl=1500+200*iv+((vt*iv)*0.05)
print('O salário final do corretor é:', sl)

