#Exercício 2

vm=float(input('Qual a velocidade de um carro?'))
mu=(vm-80)*7

if vm<=80:
    print('Você está dentro do limite de velocidade.')
else:
    print('Você foi multado em R${}.'.format(mu))

