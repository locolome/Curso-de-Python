n1=float(input('Digite a nota 1 do aluno: '))
n2=float(input('Digite a nota 2 do aluno: '))
me=(n1+n2)/2
if me<5.0:
    print('REPROVADO!')
if me>=5 and me<=6.9:
    print('RECUPERAÇÃO!')
if me>=7:
    print('APROVADO!')