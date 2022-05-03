'''lista=[]
while True:
    g=int(input('Digite um número ímpar inteiro \n(Digite 0 para finalizar):'))
    lista.append(g)
    if g==0:
        break

a=len(lista)
b=a/2-1
for index,num in enumerate(lista):
    if index==b:
        e=num
        break
fat = 1
i = 2
while i <= e:
    fat = fat*i
    i = i + 1
print(f'{e} está no meio de lista e seu fatorial é {fat}.')'''

n=int(input('digite um número ímpar, maior que 1: '))

if n<=1 or n%2==0:
    print('Número informado não atende os criterios definidos.')
else:
    l=[]
    for x in range (n):
        num=int(input('digite um numero maior ouy igual a zero: '))
        l.append(num)

centro=int(len(1/2))
ele=l[centro]
fat=1
for n in range(2,ele+1):
    fat*=n
print(f'Lista: {l}')
print(f'O elemento no centro é {centro} e seu fatorial é {fat}.')