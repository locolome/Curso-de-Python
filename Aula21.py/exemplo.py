dias=('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado' )
dia=()
print(type(dias))
print(dias[3])

texto = 'python'
print(tuple(texto))

lista=['python']
lista[2]=8
print(tuple(lista))

lista=[3,5]
tupla1=(1,2,lista)
tupla2=(1,2,lista[0],lista[1])
print(tupla)
print(tupla[2])
print(len(tupla))
print(tupla2.count(2))

lista=['python', 1, 2, 'java']
print(lista)

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

n=1
while n<4:
    mes=int(input('Escolha um mês [1-12]: '))
    if 1<=mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1
meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print(meses[:4])
print(meses[4:])
print(meses[:-4])
print(meses[-4:])

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

meses.append('janaina')

print(meses*2)

meses+=(['janaina', 'zé'])
print(meses)

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for mes in meses:
    print(mes, end=' ')


