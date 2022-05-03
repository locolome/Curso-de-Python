'''import random
alu1=input('Informe o nome do aluno 1:')
alu2=input('Informe o nome do aluno 2:')
alu3=input('Informe o nome do aluno 3:')
alu4=input('Informe o nome do aluno 4:')

lista= [alu1,alu2,alu3,alu4]

print('A ordem de apresentação é: ',random.choices(lista, k=4))'''

from random import shuffle
alu1=input('Informe o nome do aluno 1:')
alu2=input('Informe o nome do aluno 2:')
alu3=input('Informe o nome do aluno 3:')
alu4=input('Informe o nome do aluno 4:')
lista= [alu1,alu2,alu3,alu4]
shuffle(lista)
print('A ordem de apresentação é: {},{},{} e {}.'.format(lista[0],lista[1],lista[2],lista[3]))



