from random import randint



'''def sorteia():
    numeros=[]
    a=0
    for c in range(5):
        a=randint(1,10)
        numeros.append(a)
    return numeros


def somapar(numeros):
    soma=0
    
    for c in numeros:
        if c%2==0:
            soma=soma+numeros
    return soma
    
print(somapar(sorteia()))'''

def sorteia(lista):
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)

def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista} temos {soma}')

numeros=list()
sorteia(numeros)
somapar(numeros)
