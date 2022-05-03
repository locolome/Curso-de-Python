frase=input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')+1))

'''frase=input('Digite uma frase: ')
cont=frase.count('a')
pr=frase.find('a')
pre=frase.rfind('a')
print('Há {} letras "a" na frase, a primeira e ultima letra "a" estão em {} e {}'.format(cont,pr,pre))'''
