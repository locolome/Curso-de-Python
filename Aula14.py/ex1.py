from datetime import date
atual=date.today().year
ma=0
me=0
for c in range(1,8):
    a=int(input('Digite a data de nascimento: '))
    i=atual-a
    if i<18:
        me+=1
    else:
        ma+=1
print('{} pessoas atingiram maioridade e {} pessoas não atingiram maioridade.'.format(ma,me))
    