

'''n=int(input('Digite um número inteiro: '))

maior=n
menor=n
soma=0
soma+=n
cont=1

while True:
    n=int(input('Digite um número inteiro: '))
    per=input('Você quer continuar a digitar valores? [S/N] ').strip().upper()
    soma+=n
    cont+=1
    if maior<n:
        maior=n
    if menor>n:
        menor=n
    if per=='N':
        break
media=(soma)/cont
print(f'O menor valor lido foi {menor}, o maior valor lido foi {maior} e a média entre os números é {media}.')'''
resp='S'
soma=quant=media=maior=menor=0
while resp in 'S':
    num=int(input('Digite um número: '))
    soma+=num
    quant+=1
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=input('Quer continuar? [S/N]').upper().strip()
media=soma/quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')

