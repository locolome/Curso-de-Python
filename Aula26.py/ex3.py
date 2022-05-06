
'''def maior(lista):
    maiorv=0
    for valor in lista:
        if valor==0:
            maiorv=valor
        elif valor>maiorv:
            maiorv=valor
    return maiorv

lista=[0,1,2,3,4,5,6,7,8,9]

print(maior(lista))'''

def maior(*num):#receber os valores sem precisar da lista
    maior=cont=0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont==0:
            maior=valor
        elif valor>maior:
            maior=valor
        cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado é {maior}.')

#programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)


