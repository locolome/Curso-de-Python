tupla=('maçã',2,'banana',4,'pera',1,'uva',11,'mamão',12)
for c in range(0,len(tupla)):
    if c%2==0:
        print(tupla[c],end=' ')
    else:
        print(f'= R${tupla[c]},00')