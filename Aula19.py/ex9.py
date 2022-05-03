print('Nota máxima: 10')
print("Aprovado: acima de 6.")
print('Reprovado: abaixo de 6.')
a=0
for c in range(1,7):
    n1=float(input(f'Digite a nota 1 do aluno {c}: '))
    n2=float(input(f'Digite a nota 2 do aluno {c}: '))
    media=(n1+n2)/2
    print(f'A média do aluno é {media}.')
    if media<6:
        a+=1
print(f'Há {a} alunos em Prova final.')
