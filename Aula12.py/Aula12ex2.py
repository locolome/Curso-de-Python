'''nome=input('Digite o nome de uma pessoa: ')
sp=nome.find('Dias')
if sp!= -1:
    print('A pessoa tem o nome "Dias".')
else:
    print('A pessoa não tem o nome "Dias".')'''

nome=input('Digite o nome de uma pessoa: ')
print('Seu nome tem DIAS? {} '.format('DIAS' in nome.upper()))
