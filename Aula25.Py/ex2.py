tupla=('abacate','pera','uva','manga','banana')
for index,nome in enumerate(tupla):
    tup=[i for i in nome if i in['a','e','i','o','u']]
    print(f'{nome} tem as vogais: ',tup)



