p=int(input("Primeiro elemento: ") )
r = int(input("Razão: ") )

'''u = p + (10-1)*r
u = u + 1'''

d=p+9*r

for c in range(p,d+r,r):
    print('{}'.format(c),end='->')
print('Acabou')