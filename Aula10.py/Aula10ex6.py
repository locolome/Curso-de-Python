import random
x=int(input('Vamos jogar jokenpô! O que você irá jogar? \n Digite: 1 para pedra. \n 2 para papel.\n 3 para tesoura.'))
lista=('pedra','papel','tesoura')
l=random.randint(0, 2)
print('Eu joguei {}.'.format(lista[l]))
if x==1:
    if l==1:
        print('Empatou!')
    elif l==2:
        print('Você ganhou!')
    elif l==0:
        print('Você perdeu!')
elif x==2:
    if l==2:
        print('Empatou!')
    elif l==0:
        print('Você ganhou!')
    elif l==1:
        print('Você perdeu!')

elif x==0:
    if l==0:
        print('Empatou!')
    elif l==1:
        print('Você ganhou!')
    elif l==2:
        print('Você perdeu!')

