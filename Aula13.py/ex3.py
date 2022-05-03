soma=0
cont=0
for c in range(501):
  if c%3==0 and c%2!=0:
    soma=soma+c

print(soma)

soma=0
cont=0
for c in range(1,501):
  if c%3==0: 
    if c%2!=0:
      soma+=c
      cont+=1
      print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma))

