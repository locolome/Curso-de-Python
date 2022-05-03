fr=input('Digite uma frase: ').strip().upper()

palavras=fr.split()#Separar as palavras uma a uma: apos a sopa
junto=' '.join(palavras)#aposasopa
inverso=junto[::-1]
'''inverso=' '
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]'''
print(f'Inverso de {junto} é {inverso}.')
if inverso==junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')





