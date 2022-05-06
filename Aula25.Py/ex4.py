from binascii import a2b_base64
from random import randint


jogos=int(input('Quantos jogos serão criados? '))
l=[]
for c in range(jogos):
    a1=randint(1,60)
    a2=randint(1,60)
    a3=randint(1,60)
    a4=randint(1,60)
    a5=randint(1,60)
    a6=randint(1,60)
    l.append(a1)
    l.append(a2)
    l.append(a3)
    l.append(a4)
    l.append(a5)
    l.append(a6)

print(l)