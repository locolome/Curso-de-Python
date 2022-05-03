s=input('Digite seu sexo: ').strip().upper()
while s not in 'MF':
    s=(input('Caracter inválido. Digite novamente... ')).upper()
    if s=='M' or s=='F':
        break

        

