from heapq import merge
from statistics import median


'''menor=0
for c in range(1,6):
    no=input('Informe o nome do medicamento: ')
    pr=float(input('Informe o preço do medicamento:'))
    if c==1:
        menor=pr
        nom=no
        pr1=pr
    elif c==2:
        pr2=pr
        if  menor>pr:
            menor=pr
            nom=no
    elif c==3:
        pr3=pr
        if  menor>pr:
            menor=pr
            nom=no
    elif c==4:
        pr4=pr
        if  menor>pr:
            menor=pr
            nom=no
    elif c==5:
        pr5=pr
        if menor>pr:
            menor=pr
            nom=no
    else:
        if menor>c:
            menor=c
            nom=no
media=(pr1+pr2+pr3+pr4+pr5)/5

print('O medicamento mais barato é {} e seu preço é {}.'.format(nom,menor))
print('A média aritmética dos preços informados é {}.'.format(media))'''
soma=0

medicamento=input('Medicamento: ')
preco=float(input('R$: '))

maisbarato=medicamento
menorpreco=preco

soma+=preco

for x in range(4):
    medicamento=input('Medicamentos: ')
    preco+float(input('R$: '))
    if preco<menorpreco:
        menorpreco=preco
        maisbarato=medicamento
    soma+=preco
media=soma/5

print(f'{maisbarato} é o medicamento mais barato e custa R${menorpreco}.\n Média dos preços: {media}.')