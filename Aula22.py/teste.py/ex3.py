from random import choice, shuffle
lista=[]

while True:
    g=input('Digite o comprador da rifa \n(Digite 0 para finalizar.): ')
    lista.append(g)
    if g=='0':
        break

shuffle(lista)
sorteado=choice(lista)
print(f'O vencedor é {sorteado}.')


