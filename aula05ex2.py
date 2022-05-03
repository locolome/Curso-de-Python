#Exercício 2
#o=float(input('Digite o cateto oposto:'))
#a=float(input('Dgite o cateto adjacente:'))
#h=(o**2 + a**2)**(1/2)
#print('O valor da hipotenusa é de: {}'.format(h))

from math import hypot
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('Comprimento do cateto adjacente:'))
hy= hypot(co,ca)
print('A hipotenusa vai medir {:.2f}' .format(hy))