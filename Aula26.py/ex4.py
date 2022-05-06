from random import randint



def sorteia():
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
    
print(somapar(sorteia()))
