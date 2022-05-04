

'''primeiro=int(input('Digite o primeiro termo da PA: '))
print('=='*20)
qnt=int(input('Digite a quantidade de termos da PA: '))
print('=='*20)
r=int(input('Digite a razão da PA: '))
print('=='*20)

qnt=qnt+1
a=primeiro + (qnt-1)*r
a=a-1

lista=[]
soma=0
for c in range(primeiro,a,r):
    lista.append(c)
    soma=soma+c
print(lista)
print(f'A soma é {soma}')'''

termo=int(input('Digite o primeiro termo da PA: '))
print('=='*20)
num_termos=int(input('Digite a quantidade de termos da PA: '))
print('=='*20)
razao=int(input('Digite a razão da PA: '))
print('=='*20)

pa = [termo]

termo_anterior=termo

for x in range(num_termos-1):
    termo_atual=termo_anterior+razao
    pa.append(termo_atual)
    termo_anterior=termo_atual
print(pa)

soma=sum(pa)

print(f'Soma dos elementos da PA = {soma}')



