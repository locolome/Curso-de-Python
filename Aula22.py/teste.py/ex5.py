from statistics import geometric_mean
from math import sqrt

lista=[]
a=int(input('Digite um valor \n(ou 0 para finalizar): '))
lista.append(a)
maior=a
menor=a

while True:
    a=int(input('Digite um valor \n(ou 0 para finalizar): '))
    
    if a==0:
        break
    lista.append(a)



for index,num in enumerate(lista):
    if num>maior:
        maior=num
    if num<menor:
        menor=num

b=round(geometric_mean([menor,maior],))

print(f'A média geométrica de {menor} e {maior} é {b}.')

lista=[9,3,5,7,2,1]

menor=min(lista)
maior=max(lista)
media_geo=sqrt(menor*maior)
print(f'Lista: {lista}')
print(f'Média gometrica entre {menor} e {maior} é igual a {media_geo} ')

    

