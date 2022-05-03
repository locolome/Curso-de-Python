lista=['Janaiana', 'José', 'Maria', 'Carlos']
listaa=['José', 'Pedro']
for n in range(0, len(lista)):

lista.append('Jorge')#adiciona no final

lista.insert(0, 'Jorge')#adiciona com precisão

lista.sort()#ordena crescente

lista.sort(reverse=True)#ordena decrescente

del lista[-1]#deleta com precisão

lista.remove('Janaiana')#deleta só a palavra 

lista.pop()#exclui o ultimo ou outro

lista.clear()#limpa

listaa=lista#linka

listaa=lista[:]#linka na cópia, não no original

lista.extend(listaa)#junta as duas listas

print(lista.count('José'))

print(len(lista))

print(lista.index('Janaiana'))

for indice,nome in enumerate(lista):
    print(f'{nome} está armazanado no índice {indice}')

a=[[2,1,-5],[3,7,0],[6,4,8]]
print(a[0][0],a[0][1],a[0][2])
print(a[0][0]+a[0][1]+a[0][2])
print(listaa)
soma_a=0
lin=len(a)
col=len(a[0])
for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]
print(soma_a)