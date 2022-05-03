a=int(input('Digite um valor: '))
b=int(input('Digite um valor: '))
c=int(input('Digite um valor: '))
d=int(input('Digite um valor: '))
tupla=(a,b,c,d)
cont=0

'''if 9 in tupla:
    print(f'O valor aparece {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O número 3 foi digitado {tupla.index(3)+1}ª pocição.')'''


for index in range(0,len(tupla)):
    if tupla[index]==9:
        cont+=1

print(f'Há {cont} vezes o número 9.')
    
for indice,nome in enumerate(tupla):
    if nome==3:
        print(f'O primeiro valor três foi digitado em {indice}.')

for a in range(0,len(tupla)):
    if tupla[a]%2==0:
        print(f'Os números pares são {tupla[a]}.')       





