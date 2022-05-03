cont=0
soma=0
num=0
num=int(input('Digite um número ou 999 para parar: '))
while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
'''while True:
    n=int(input('Digite um número inteiro: '))
    cont+=1
    if n!=999:
        soma+=n
    if n==999:
        break
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')'''

