pe=float(input('Digite seu peso: '))
al=float(input('Digite sua altura: '))
imc=pe/al**2
print('Seu peso é de: ',imc)
if imc<=18.5:
    print('Você está abaixo do peso.')
if imc>18.5 and imc<=25:
    print('Você está no peso ideal.')
if imc>25 and imc<=30:
    print('Você está com sobrepeso.')
if imc>30 and imc<=40:
    print('Você está em obesidade.')
if imc>40:
    print('Você está em obesidade mórbida.')