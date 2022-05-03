km=float(input('Qual a quantidade de kms percorridos?'))
dia=float(input('Qual a quantidade de dias pelos quais ele foi alugado?'))
pr=((km*0.15)+(dia*60))
print('O preço a pagar será de R${:.2f}.'.format(pr))

