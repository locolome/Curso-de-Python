from math import radians,sin,cos,tan
angulo=float(input('Digite o ângulo desejado:'))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))
print('Para o ângulo {:.2f}, o seno é {:.2f}, o cosseno é {:.2}, e a tangente é {:.2f}.'.format(angulo,seno,cosseno,tangente))


