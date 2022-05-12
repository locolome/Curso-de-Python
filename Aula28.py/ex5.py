from MinhasFuncoes import *
masc=0
fem=0
for c in obtem_dados_funcionarios():
    if c=='M':
        masc+=1
    elif c=='F':
        fem+=1
print(f'Há {masc} homens e {fem} mulheres cadastrados.')
