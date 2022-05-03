#Exercício 4
nome=input('Digite seu nome completo:')
x=nome.lower()
y=nome.upper()
print ('Seu nome completo com as letras minúsculas é: {}, e com as letras maiúsculas é: {}'.format(x,y))
l=len(nome)- nome.count(' ')
print('Seu nome têm {} letras ao todo'.format(l))
pr= nome.find(' ')
print('Seu primeiro nome tem: {} letras.'.format(pr))