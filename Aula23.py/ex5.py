nad=[]
temp=[]
n=input('Digite o nome do nadador: ')
t=int(input('Digite o tempo do nadador: '))
nad.append(n)
temp.append(t)
maiorna=n
menorna=n
maiortemp=t
menortemp=t
soma=0

for c in range(0,6):
    n=input('Digite o nome do nadador: ')
    nad.append(n)
    t=int(input('Digite o tempo do nadador: '))
    temp.append(t)
    soma=soma+t
    if t<menortemp:
        menortemp=t
        menorna=n
    if t>maiortemp:
        maiortemp=t
        maiorna=n

media=soma/7
print(f'O nadador com o pior tempo é {maiorna} com {maiortemp} segundos.')
print(f'O nadador com o melhor tempo é {menorna} com {menortemp} segundos.')
print(f'A média dos tempos é {media}.')       
