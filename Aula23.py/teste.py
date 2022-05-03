'''#converter tupla em lista
dias=('domingo','segunda','terça','quarta','quinta','sexta','sabado')

semana=list(dias)

print(f'A variavel semana é do tipo {type(semana)} e contem os dias da semana {semana}')'''

num=[]
for n in range(0,10):
    num.append(n**2)
print(num)

#lista comprimidas
lista1=[x**2 for x in range(10)]#inserindo na lista os numeros entre 0 a 10 elevado ao quadrado
print(lista1)

lista2=[x for x in range(1,20)if x%2==0]#inserido na lista os numeros pares no intervalo de 0 a 20
print(lista2)

lista3=[i for i in "HACKATHON" if i in['A','E','I','O','U']]#descobrir as vogais da palavra da lista
print(lista3)

lista4=[1,2,3]
lista4=[i**3 for i in lista4]#atribuir novos valores aos elementos da lista atraves de uma operaçao 
print(lista4)