vc=float(input('Qual o valor da casa?'))
sc=float(input('Qual o salário do comprador?'))
an=float(input('Em quantos anos o comprador ele vai pagar?'))
me=an*12
por=sc*0.3
ve=vc/me
if ve>por:
    print('O empréstimo foi negado.')
else:
    print('O empréstimo foi aprovado')
    
