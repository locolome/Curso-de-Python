lista = [12, -2, 4, 8, 29,45,78,36,-17,2,12,8,3,3,-52]
maiorvalor=lista[0]
menorvalor=lista[0]
listapares=[]
ocorrencia=0
mediaelementos=0
somanegativo=0
for index in range(0,len(lista)):
    #maior alor
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]
    #menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #números pares
    if lista[index]%2==0:
        listapares.append(lista[index])
    #ocorrencia do primeiro item
    if lista[index]==lista[0]:
        ocorrencia+=1
    #media
    mediaelementos+=lista[index]
    #soam dos negativos
    if lista[index]<0:
        somanegativo+=lista[index]
mediaelementos/=len(lista)
print(f'Maior elemento: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listapares}')
print(f'Número de ocorrências do primeiro item: {ocorrencia}')
print(f'A média dos elementos é : {mediaelementos}')
print(f'Elementos negativos: {somanegativo}')