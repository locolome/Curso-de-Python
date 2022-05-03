
ho18=0
mu=0
id=int(input('Informe a idade do aluno:'))
while id>0:
    se=input('Informe o sexo do aluno [M/F]: ').strip().upper()
    id=int(input('Informe a idade do aluno:'))
    if id<0:
        print('Encerrando programa...')
    if id>18 and se=='M':
        ho18+=1
    elif se=='F':
        mu+=1
print('Há {} homens acima de 18 anos, e há {} mulheres.'.format(ho18,mu))   