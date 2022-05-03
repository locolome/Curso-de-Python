
num=int(input('Digite um número inteiro positivo:'))
pa=num**2
im=num**3

if (num%2) == 0:
    print('O quadrado de {} é {}.'.format(num,pa))
else:
    print('O cubo de {} é {}.'.format(num,im))
    
