#Exercício 4
'''di=float(input('Digite a distância da viagem:'))
p1=di*0.50
p2=di*0.45
if di> 200:
    print('O preço da passagem será {}.'.format(p2))
else:
    print('O preço da passagem será {}.'.format(p1))'''
dis=float(input('Qual a distância da sua viagem:'))
pr=dis*0.5 if dis<=200 else dis*0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(pr))

    