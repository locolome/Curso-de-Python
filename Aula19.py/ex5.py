from random import randint
from re import X
cont=0
soma=0
print('\033[31mVamos jogar ímpar ou par!\033[m')
while True:
    esc=input('Escolha ímpar ou par: ').strip().upper()   
    n=int(input('Escolha seu número...'))
    x=randint(0,10)
    soma=n+x
        
    if esc=='ÍMPAR':
        if soma%2==0:
            print(f"Você perdeu, mas teve {cont} vitórias consecutivas!")
            break
        if soma%2!=0:
            cont+=1
            print('\033[3;31;36mVocê venceu!\033[m')
    if esc=='PAR':
        if soma%2==0:
            print(f'\033[3;31;36mVocê venceu!\033[m')
            cont+=1
        if soma%2!=0:
            print(f'Você perdeu, mas teve {cont} vitórias consecutivas!')
            break
