
from cmath import sqrt
from random import randrange
from statistics import geometric_mean

n=int(input('Informe um valor: '))
l=[]
l=[randrange(n) for i in range(n)]
print(l)
for c in l:
    mul=1
    mul=mul*c

a=mul**(1/len(l))
print(a)