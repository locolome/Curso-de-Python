



#id=int(input('Informe a idade de um aluno: '))
idade=int(input('Idade: '))
maior=id
menor=id

while True:
    idade=int(input('Idade: '))
    if idade<0:
        break
    if idade<menor:
        menor=idade
    elif idade>maior:
        maior=idade

media=(menor+maior)/2

print(f'Menor idade: {menor}\n Maior idade: {maior} \n Média das idades:{media:.2f}')

'''while id>0:
    id=int(input('Informe a idade de um aluno: '))
    if id<0:
        break
    if maior<id:
        maior=id
    if menor>id: 
        menor=id
media=(menor+maior)/2
print('A média aritmética entre {} e {} é {}.'.format(maior,menor,media))'''