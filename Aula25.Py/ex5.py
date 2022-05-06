from random import randrange


linha=int(input('Número de linhas: '))
colunas=int(input("Número de colunas: "))
soma=0
a=[[randrange(0,2) for i in range(colunas)] for j in range (linha)]

for i in range(linha):
    for j in range(colunas):
        print(a[i][j], end=' ')
        soma+=(a[i][j])
    print()
if soma==0:
    print('Matriz nula')


