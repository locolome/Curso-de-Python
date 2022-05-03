
'''menor=0
maior=0
qnt=0
nom=" "
for c in range(1,8):
    na=input('Digite o nome do nadador: ')
    t=float(input('Digite o tempo do nadador: '))
    if t>=12 and t<=15:
        qnt+=1
    if c==1:
        menor=t
        nom1=na
        maior=t
        nom2=na
        na1=t
    elif c==2:
        na2=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
    elif c==3:
        na3=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
    elif c==4:
        na4=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
    elif c==5:
        na5=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
    elif c==6:
        na6=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
    elif c==7:
        na7=t
        if menor>t:
            nom1=na
            menor=t
        if maior<t:
            nom2=na
            maior=t
media=(na1+na2+na3+na4+na5+na6+na7)/7
print(f'O nadador com o pior tempo é {nom1} com {menor}s.')
print(f'O nadador com o melhor tempo é {nom2} com {maior}s.')
print(f'O tempo médio dos nadadores é de {media}s.')
print(f'A quantidade de nadadores com tempo entre 12s e 15s é de {qnt}.')'''
nome=input('Nadador 1 : ')
tempo=float(input('Tempo do nadador 1: '))

melhornadador=nome
melhortempo=tempo
piornadador=nome
piortempo=tempo

somatempo=0
somatempo+=tempo
tempo12e15=0

if 12<= tempo <=15:
    tempo12e15+=1

for nadador in range(2,8):
    nome=input(f'Nadador {nadador}: ')
    tempo=float(input(f'Tempo do nadador {nadador}: '))

    if tempo<melhortempo:
        melhornadador=nome
        melhortempo=tempo
    elif tempo>piortempo:
        piornadador=nome
        piortempo=tempo
    
    somatempo+=tempo

    if 12<=tempo<=15:
        tempo12e15+=1

print(f'{melhornadador} é o melhor nadador com {melhortempo} seg. \n{piornadador} é o pior nadador com {piortempo} seg. ')
media=somatempo/7
print(f'Média dos tempos= {media:.2f} seg. \n Atletas entre 12 e 15 seg. : {tempo12e15}')



