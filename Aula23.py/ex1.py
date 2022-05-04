'''ordem=int(input('Digite a ordem: '))
matriz= [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,ordem):
    for c in range(0,ordem):
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}] '))
for l in range(0,ordem):
    for c in range(0,ordem):
        print(f'[{matriz[l][c]:^5}]' ,end=' ')
    print()
'''

from random import randrange

linha=int(input('Número de linhas: '))
colunas=int(input("Número de colunas: "))

a=[[randrange(1,11) for i in range(colunas)] for j in range (linha)]
b=[[randrange(1,11) for i in range(colunas)] for j in range (linha)]

abaixodp=0
acimadp=0
for i in range(linha):
    for j in range(colunas):
        if i>j:
            abaixodp+=a[i][j]
        if i<j:
            acimadp+=b[i][j]
print('Matriz A: ')
for i in range(linha):
    for j in range(colunas):
        print(a[i][j], end=' ')
    print()
print('Matriz B')
for i in range(linha):
    for j in range(colunas):
        print(b[i][j], end=' ')
    print()
print(f'Soma= {abaixodp+acimadp}')