
from tkinter import N


q=int(input('Quantos números você quer digitar?'))
soma=0

'''for c in range(0,q):
    soma=soma+c
media=soma/q
print('A média aritmética de {} é {}.'.format(q,media))'''

for cont in range(q):
    num=float(input('Digite um número:' ))
    soma+=num
media=soma/q
print('Média = {:.2f}'.format(media))
    




