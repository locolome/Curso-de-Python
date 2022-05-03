import random
r=(random.randint(0,11))
print('O computador irá pensar em um número de 0 a 10, tente adivinha-lô!')
#n=int(input('Digite seu número: ')) 
palp=0
'''while n!=r:
    n=int(input('Você errou, tente novamente...'))
    palp+=1'''
acertou=False
while not acertou:
    jogador=int(input('Qual seu palpite? '))
    palp+=1
    if jogador==r:
        acertou=True
    else:
        if jogador>r:
            print('Menos... tente mais uma vez')
        elif jogador<r:
            print('Mais... tente novamente.')

print('Você acertou!')
print('Foram necessários para vencer {} palpites.'.format(palp))
