#Exercício 1
num=int(input('Digite um número:'))
ss=(num+1)
an=(num-1)
print('O sucessor e antecessor de',num,'são, respectivamente,{} e {}'.format(ss,an))

#Exercício 2
num=float(input('Digite um número:'))
tri=(num*3)
dob=(num*2)
raiz=(num**0.5)
print('O dobro de {} vale {}. \n o triplo de {} vale {}. \n A raíz quadrada de {} vale {}.' .format(num,dob,num,tri,num,raiz))
#print('A raíz quadrada, dobro e triplo de {} são, respectivamente, {} , {} e {}.'.format(num,raiz,tri,dob))


#Exercício 3
ds=float(input('Qual a variação do deslocamento do objeto?'))
tm=float(input('Qual a variação do tempo percorrido?'))
vm=(ds/tm)
print('A velocidade média é igual a {:.4f} m/s'.format(vm))
#print('A velocidade média do objeto é de:',vm)

#Exercício 4
pu=float(input('Qual o preço unitário da peça?'))
qv=float(input('Qual a quantidade vendida?'))
tv=(pu*qv)
#co=(5%tv)
co=(tv*0.05)
print('O valor do pagamento da comissão é de:',co)

#Exercício 5
ra=float(input('Qual o raio do círculo?'))
#ar=(3.14*ra*ra)
ar=(3.14*ra**2)
print('A área do círculo é de:',ar)
