
#Exercício 1
import random
r=(random.randint(0,5))
x=int(input('Adivinhe o número escolhido de 0 a 5 pelo computador:'))
if x==r:
    print('Você acertou o número!')
else:
    print('Você errou o número!')
