def somarElementoslista(inteiros):#somar os elementos da lista
    soma=0
    for valor in inteiros:
        soma+=valor
    return soma
lista=[1,2,3,4,5,6]
print(somarElementoslista([3,4,6,9,10,23,13]))
print(somarElementoslista([lista]))
