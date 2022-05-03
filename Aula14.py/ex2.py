maior=0
maior=0
for c in range(1,6):
    p=float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if p==1:
        maior=p
        menor=p
    else:   
        if maior<p:
            maior=p
        if menor>p:
            menor=p 
print('O maior peso é {} e o menor peso é {}.'.format(maior,menor))
    
