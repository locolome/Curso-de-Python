import random
alu1=input('Informe o nome do aluno 1:')
alu2=input('Informe o nome do aluno 2:')
alu3=input('Informe o nome do aluno 3:')
alu4=input('Informe o nome do aluno 4:')
lista= [alu1,alu2,alu3,alu4]
l= random.choice(lista)
print('O aluno sorteado foi:{} '.format(l))
